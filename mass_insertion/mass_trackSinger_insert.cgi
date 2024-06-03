#!/usr/bin/ruby
# FILE: mass_trackSinger_insert.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
# 
#
require 'cgi'
require 'stringio'
require 'mysql2'

$stdout.sync = true
$stderr.reopen $stdout

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
 	song_title = field[0]
	group_name = field[1]
	stage_name = field[2]
	
	# must obey all foreign key constraints by going in proper order
	# using INSERT IGNORES to avoid error popups that have no effect (ex. duplicates, but dupes arent put in).
	# ignore referenced by https://www.mysqltutorial.org/mysql-insert-ignore/

	insertTrackSingerBand = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")

	insertTrackSingerArtist = db.query("INSERT IGNORE INTO Artist(stage_name, group_name) 
	VALUES ('" + stage_name + "','" + group_name + "');")

	insertTrackSingerSong = db.query("INSERT IGNORE INTO Song(song_title, group_name) 
	VALUES ('" + song_title + "','" + group_name + "');")
	
	insertTrackSinger = db.query("INSERT INTO trackSinger(song_title, group_name, stage_name) 
	VALUES ('" + song_title + "','" + group_name + "','" + stage_name + "');")

end

# successful landing page		
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='20; url=trackSingers.html'>"
print "<TITLE>Track Singer Upload Done</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Track Singer insert completed! </H1>\n"
print "Uploaded: <br>" + originalName
print "</BODY>\n"
print "</HTML>\n"
