#!/usr/bin/ruby
# FILE: trackSingerSelect.cgi
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
	if (cgi['trackSinger_sort'] == 'Unordered')
		trackSingerSelect = db.query "SELECT * FROM trackSinger"
	end

	if (cgi['trackSinger_sort'] == 'Stage Name Alphabetical Order')
		trackSingerSelect = db.query "SELECT * FROM trackSinger ORDER BY stage_name"
	end

	if (cgi['trackSinger_sort'] == 'Group Name Alphabetical Order')
		trackSingerSelect = db.query "SELECT * FROM trackSinger ORDER BY group_name"
	end

	if (cgi['trackSinger_sort'] == 'Song Title Alphabetical Order')
		trackSingerSelect = db.query "SELECT * FROM trackSinger ORDER BY song_title"
	end
	
puts "<!DOCTYPE html>"
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Track Singers </title>"

	puts "<p style='text-align:center; font-size:30px;'> TRACK SINGERS <br> You might want to scroll down... <br> </p> <tr> <th> SONG TITLE </th>"
	puts " <th> GROUP NAME </th> <th> STAGE NAME  </th> </tr>"
	trackSingerSelect.each do |row|
			puts "<br> <tr>"
			# datatypes must be converted into strings, especially for NULLS
			puts "<td> " + row['song_title'].to_s + "</td>" + " " + "<td>" + row['group_name'].to_s + "</td>" + " " + "<td>" + row['stage_name'].to_s + "</td>"
			puts "<br> </tr>"
		end