#!/usr/bin/ruby
# FILE: manual_insert_song.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
#
# sequence for error output
require 'cgi'
require 'mysql2'
$stdout.sync=true
$stderr.reopen $stdout
print "content-type: text/html\r\n\r\n"
cgi = CGI.new ("html5")

db = Mysql2::Client.new(
	:host=> '10.20.3.4',
	:username=> 'dbms_em',
	:password=> 'em_moorman',
	:database=> 'dbms_em_dbA'
)

	song_title = cgi['song_title']
	release_date = cgi['release_date']
	group_name = cgi['group_name']
	track_type = cgi['track_type']
	language = cgi['language']
	album_name= cgi['album_name']

	bandInsert = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")
	
	albumInsert = db.query("INSERT IGNORE INTO Album(group_name, album_name) 
	VALUES ('" + group_name + "','" + album_name + "');")

	songInsert = db.query("INSERT INTO Song(song_title, release_date, group_name, track_type, language, album_name) 
	VALUES ('" + song_title + "','" + release_date + "','" + group_name + "','" + track_type + "','" + language + "','" + album_name + "');")

print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=manual_insert_song.html'>"
print "<TITLE>Song Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Song Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
