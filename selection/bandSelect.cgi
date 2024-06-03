#!/usr/bin/ruby
# FILE: bandSelect.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
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

	#Sorting Conditionals
	if (cgi['band_sort'] == 'Unordered')
		bandSelect = db.query "SELECT * FROM Band"
	end

	if (cgi['band_sort'] == 'Alphabetical Order')
		bandSelect = db.query "SELECT * FROM Band ORDER BY group_name"
	end

	if (cgi['band_sort'] == 'Ascending Group Debut Date')
		bandSelect = db.query "SELECT * FROM Band ORDER BY group_debut_date"
	end

	if (cgi['band_sort'] == 'Descending Group Debut Date')
		bandSelect = db.query "SELECT * FROM Band ORDER BY group_debut_date DESC"
	end

	if (cgi['band_sort'] == 'Ascending Number of Members')
		bandSelect = db.query "SELECT * FROM Band ORDER BY number_of_members"
	end

	if (cgi['band_sort'] == 'Descending Number of Members')
		bandSelect = db.query "SELECT * FROM Band ORDER BY number_of_members DESC"
	end


# webpage html
puts "<!DOCTYPE html>"
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Bands </title>"

	puts "<p style='text-align:center; font-size:30px;'> BANDS <br> You might want to scroll down... <br> </p> <tr> <th> GROUP NAME </th>"
	puts " <th> LABEL NAME </th> <th> GROUP DEBUT DATE  </th>  <th> NUMBER OF MEMBERS  </th> </tr>"
	bandSelect.each do |row|
			puts "<br> <tr>"
			# datatypes must be converted into strings
			puts "<td> " + row['group_name'].to_s + "</td>" + " " + "<td>" + row['label_name'].to_s + "</td>" + " " + "<td>" + row['group_debut_date'].to_s + "</td>" + " " + "<td>" + row['number_of_members'].to_s + "</td>"
			puts "<br> </tr>"
	end

puts "</table>"
puts "</body>"
puts "</html>"
