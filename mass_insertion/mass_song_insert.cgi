#!/usr/bin/ruby
# FILE: mass_song_insert.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
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
    field = line.split(',')
    song_title = field[0]
    release_date = field[1]
    group_name = field[2]
    track_type = field[3]
    language= field[4]
    album_name = field[5]

	#if date is null, need to make it a string to not cause type error
	if release_date == "NULL" 
	release_date.to_s = "NULL"
	end
	
	insertSongBand = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")
	
	insertSongAlbum = db.query("INSERT IGNORE INTO Album(group_name, album_name) 
	VALUES ('" + group_name + "','" + album_name + "');")

	insertSong = db.query("INSERT IGNORE INTO Song(song_title, release_date, group_name, track_type, language, album_name) 
	VALUES ('" + song_title + "','" + release_date + "','" + group_name + "','" + track_type + "','" + language + "','" + album_name + "');")
	
end

# successful landing page		
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='20; url=songs.html'>"
print "<TITLE>Song Upload Done</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Song insert completed! </H1>\n"
print "Uploaded: <br>" + originalName
print "</BODY>\n"
print "</HTML>\n"
