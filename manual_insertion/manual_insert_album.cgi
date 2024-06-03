#!/usr/bin/ruby
# FILE: manual_insert_album.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
# Web Server Based Insert of Album
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
	# moving cgis to variables just for ease of use in the eye sores that are ruby database queries
	album_name = cgi['album_name']
	group_name = cgi['group_name']
	album_release_date = cgi['album_release_date']
	album_type = cgi['album_type']

	# make sure all foreign key constraints are not violated by inserting in proper order
	bandInsert = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")

	albumInsert = db.query("INSERT INTO Album(album_name, group_name, album_release_date, album_type) 
	VALUES ('" + album_name + "','" + group_name + "','" + album_release_date + "','" + album_type + "');")

print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=manual_insert_album.html'>"
print "<TITLE>Album Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Album Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
