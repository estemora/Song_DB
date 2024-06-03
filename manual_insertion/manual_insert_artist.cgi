#!/usr/bin/ruby
# FILE: manual_insert_artist.cgi
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
	
	# moving user inputs into more concise variables for ease of use
	stage_name = cgi['stage_name']
	group_name = cgi['group_name']
	legal_name = cgi['legal_name']
	birthdate = cgi['birthdate']
	debut_date = cgi['debut_date']
	
	# make sure all foreign key constraints are covered by inserting in correct order
	insertBand = db.query("INSERT IGNORE INTO Band(group_name) 
	VALUES ('" + group_name + "');")
	
	insertArtist = db.query ("INSERT INTO Artist(stage_name, group_name, legal_name, birthdate, debut_date) 
	VALUES ('" + stage_name + "','" + group_name + "','" + legal_name + "','"+ birthdate + "','" + debut_date + "');")

#
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=manual_insert_artist.html'>"
print "<TITLE>Artist Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Artist Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
