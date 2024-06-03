#!/usr/bin/ruby
# FILE: mass_artist_insert.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
# Mass Insertion of Artist Entity 
#
require 'cgi'
require 'stringio'
require 'mysql2'

$stdout.sync = true
$stderr.reopen $stdout

##
print "Content-type: text/html\r\n\r\n"

uploadLocation = "/NFSHome/emora/public_html/songs_db/songsFolder/"
cgi = CGI.new("html5")  # add HTML generation methods

# create a Tempfile reference
fromfile = cgi.params['fileName'].first
originalName = cgi.params['fileName'].first.instance_variable_get("@original_filename")

# create output file reference as original filename in our chosen directory
tofile = uploadLocation + originalName 

# copy the file
# note the untaint prevents a security error
# cgi sets up an StringIO object if file < 10240
# or a Tempfile object following works for both
  
File.open(tofile.untaint, 'w') { |file| file << fromfile.read}
##

db = Mysql2::Client.new(
	:host=> '10.20.3.4',
	:username=> 'dbms_em',
	:password=> 'em_moorman',
	:database=> 'dbms_em_dbA'
)

allLines = IO.readlines(tofile)

# split strings into seperate fields for table use

allLines.each do |line| 
    field = line.split(",")
    stage_name = field[0]
    group_name = field[1]
    legal_name = field[2]
    birthdate = field[3]
    debut_date = field[4]
	
	# make sure all bases are covered, using ignore for parent tables so unneccessary error does not pop up
	# ignore referenced from https://www.mysqltutorial.org/mysql-insert-ignore/	
	insertBand = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")
	
	insertArtist = db.query ("INSERT IGNORE INTO Artist(stage_name, group_name, legal_name, birthdate, debut_date) 
	VALUES ('" + stage_name + "','" + group_name + "','" + legal_name + "','"+ birthdate + "','" + debut_date + "');")
end
		
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='20; url=artists.html'>"
print "<TITLE>Artist Upload Done</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Artist insert completed! </H1>\n"
print "Uploaded: <br>" + originalName
print "</BODY>\n"
print "</HTML>\n"
