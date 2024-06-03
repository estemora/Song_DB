#!/usr/bin/ruby
# FILE: manual_insert_label.cgi
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

	label_name = cgi['label_name']
	founding_date = cgi['founding_date']
	
		labelInsert = db.query ("INSERT INTO Label(label_name, founding_date) 
		VALUES ('" + label_name + "','" + founding_date + "');")

print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='10; url=manual_insert_label.html'>"
print "<TITLE>Label Inserted</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Label Inserted! </H1>\n"
print " <br> Redirecting..."
print "</BODY>\n"
print "</HTML>\n"
