#!/usr/bin/ruby
# FILE: albumSelect.cgi
# Estefan Mora, Transy U
# CS 3144, Winter 2023
#
# User Selection for Album Entity
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
	if (cgi['album_sort'] == 'Unordered')
		albumSelect = db.query "SELECT * FROM Album"
	end

	if (cgi['album_sort'] == 'Album Alphabetical Order')
		albumSelect = db.query "SELECT * FROM Album ORDER BY album_name"
	end

	if (cgi['album_sort'] == 'Group Alphabetical Order')
		albumSelect = db.query "SELECT * FROM Album ORDER BY group_name"
	end

	if (cgi['album_sort'] == 'Album Type Alphabetical Order')
		albumSelect = db.query "SELECT * FROM Album ORDER BY album_type"
	end

	if (cgi['album_sort'] == 'Ascending Album Release Date')
		albumSelect = db.query "SELECT * FROM Album ORDER BY album_release_date"
	end

	if (cgi['album_sort'] == 'Descending Album Release Date')
		albumSelect = db.query "SELECT * FROM Album ORDER BY album_release_date DESC"
	end
	
puts "<!DOCTYPE html>"

	# inline html since I do not believe css works with cgi
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Albums </title>"

	puts "<p style='text-align:center; font-size:30px;'> ALBUMS <br> You might want to scroll down... <br> </p> <tr> <th> ALBUM NAME  </th>"
	puts " <th> GROUP NAME  </th> <th> GROUP DEBUT DATE  </th>  <th> ALBUM TYPE  </th> </tr>"
	albumSelect.each do |row|
			puts "<br> <tr>"
			# datatypes must be converted into strings
			puts "<td> " + row['album_name'].to_s + "</td>" + " " + "<td>" + row['group_name'].to_s + "</td>" + " " + "<td>" + row['album_release_date'].to_s + "</td>" + " " + "<td>" + row['album_type'].to_s + "</td>"
			puts "<br> </tr>"
		end