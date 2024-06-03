#!/usr/bin/ruby
# FILE: manual_band_insert.cgi
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

	group_name = cgi['group_name']
	label_name = cgi['label_name']
	group_debut_date= cgi['group_debut_date']
	number_of_members = cgi['number_of_members']

	insertLabel = db.query("INSERT IGNORE INTO Label(label_name) 
	VALUES ('" + label_name + "');")

	insertBand = db.query("INSERT INTO Band(group_name, label_name, group_debut_date, number_of_members) 
	VALUES ('" + group_name + "','" + label_name + "','" + group_debut_date + "'," + number_of_members + ");")

print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=insertBand.html'>"
print "<TITLE>Band Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Band Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
