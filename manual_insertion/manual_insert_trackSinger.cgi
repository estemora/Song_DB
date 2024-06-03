#!/usr/bin/ruby
# FILE: manual_insert_trackSinger.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
#
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
	group_name = cgi['group_name']
	stage_name = cgi['stage_name']
	
	# must obey all foreign key constraints by going in proper order
	# using INSERT IGNORES to avoid error popups that have no effect (ex. duplicates, but dupes arent put in).
	# ignore referenced by https://www.mysqltutorial.org/mysql-insert-ignore/

	bandInsert = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")

	artistInsert = db.query("INSERT IGNORE INTO Artist(stage_name, group_name) 
	VALUES ('" + stage_name + "','" + group_name + "');")

	songInsert = db.query("INSERT IGNORE INTO Song(song_title, group_name) 
	VALUES ('" + song_title + "','" + group_name + "');")
	
	trackSingerInsert = db.query("INSERT INTO trackSinger(song_title, group_name, stage_name) 
	VALUES ('" + song_title + "','" + group_name + "','" + stage_name + "');")

print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=manual_insert_trackSinger.html'>"
print "<TITLE>Track Singer Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Track Singer Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
