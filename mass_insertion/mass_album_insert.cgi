#!/usr/bin/ruby
# FILE: mass_album_insert.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
# Mass Insertion of Album Entity
#
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
	album_name = field[0]
	group_name = field[1]
	album_release_date = field[2]
	album_type = field[3] 
	
	#make sure all foreign keys are covered before inserting into child table
	#insert ignore used as mentioned before to not popup unnecessary errors of duplication	
	insertAlbumBand = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")

	insertAlbum = db.query("INSERT IGNORE INTO Album(album_name, group_name, album_release_date, album_type) 
	VALUES ('" + album_name + "','" + group_name + "','" + album_release_date + "','" + album_type + "');")
end
		
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='20; url=albums.html'>"
print "<TITLE>Album Upload Done</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Album insert completed! </H1>\n"
print "Uploaded: <br>" + originalName
print "</BODY>\n"
print "</HTML>\n"
