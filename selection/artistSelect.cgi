#!/usr/bin/ruby
# FILE: artistSelect.cgi
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
	if (cgi['artist_sort'] == 'Unordered')
		artistSelect = db.query "SELECT * FROM Artist"
	end

	if (cgi['artist_sort'] == 'Alphabetical Stage Name')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY album_name"
	end

	if (cgi['artist_sort'] == 'Alphabetical Band Name')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY group_name"
	end

	if (cgi['artist_sort'] == 'Ascending Birthdate')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY birthdate"
	end

	if (cgi['artist_sort'] == 'Descending Birthdate')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY birthdate DESC"
	end

	if (cgi['artist_sort'] == 'Ascending Debut Date')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY debut_date"
	end

	if (cgi['artist_sort'] == 'Descending Debut Date')
		artistSelect = db.query "SELECT * FROM Artist ORDER BY debut_date DESC"
	end

# webpage html
puts "<!DOCTYPE html>"
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Artists </title>"

	puts "<p style='text-align:center; font-size:30px;'> ARTISTS <br> You might want to scroll down... <br> </p> <tr> <th> STAGE NAME </th>"
	puts " <th> GROUP NAME  </th> <th> LEGAL NAME  </th>  <th> BIRTHDATE  </th> <th> DEBUT DATE </th> </tr>"
	artistSelect.each do |row|
			puts "<br> <tr>"
			# datatypes must be converted into strings
			puts "<td> " + row['stage_name'].to_s + "</td>" + " " + "<td>" + row['group_name'].to_s + "</td>" + " " + "<td>" + row['legal_name'].to_s + "</td>" + " " + "<td>" + row['birthdate'].to_s + "</td>" + "<td>" + row['debut_date'].to_s + "</td>"
			puts "<br> </tr>"
	end

puts "</table>"
puts "</body>"
puts "</html>"
