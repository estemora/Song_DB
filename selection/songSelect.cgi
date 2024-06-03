#!/usr/bin/ruby
# FILE: songSelect.cgi
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

	if (cgi['song_sort'] == 'Unordered')
		songSelect = db.query "SELECT * FROM Song"
	end

	if (cgi['song_sort'] == 'Song Alphabetical Order')
		songSelect = db.query "SELECT * FROM Song ORDER BY album_name"
	end

	if (cgi['song_sort'] == 'Group Alphabetical Order')
		songSelect = db.query "SELECT * FROM Song ORDER BY group_name"
	end

	if (cgi['song_sort'] == 'Album Alphabetical Order')
		songSelect = db.query "SELECT * FROM Song ORDER BY album_name"
	end

	if (cgi['song_sort'] == 'Language Alphabetical Order')
		songSelect = db.query "SELECT * FROM Song ORDER BY language"
	end

	if (cgi['song_sort'] == 'Song Type Alphabetical Order')
		songSelect = db.query "SELECT * FROM Song ORDER BY song_type"
	end

	if (cgi['song_sort'] == 'Ascending Song Release Date')
		songSelect = db.query "SELECT * FROM Song ORDER BY release_date"
	end

	if (cgi['song_sort'] == 'Descending Song Release Date')
		songSelect = db.query "SELECT * FROM Song ORDER BY release_date DESC"
	end
	
puts "<!DOCTYPE html>"
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Songs </title>"

	puts "<p style='text-align:center; font-size:30px;'> SONGS <br> You might want to scroll down... <br></p> <tr> <th> SONG TITLE  </th>"
	puts " <th> RELEASE DATE </th> <th> GROUP NAME  </th> <th> TRACK TYPE </th> <th> LANGUAGE </th>  <th> ALBUM NAME  </th> </tr>"
	songSelect.each do |row|
			puts "<br> <tr>"
			# datatypes must be converted into strings, especially for NULLS
			puts "<td> " + row['song_title'].to_s + "</td>" + " " + "<td>" + row['release_date'].to_s + "</td>" + " " + "<td>" + row['group_name'].to_s + "</td>" + " " + "<td>" + row['track_type'].to_s + "</td>" + "<td>" + row['language'].to_s + "</td>" + " " + "<td>" + row['album_name'].to_s + "</td>"
			puts "<br> </tr>"
		end