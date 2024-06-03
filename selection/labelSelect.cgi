#!/usr/bin/ruby
# FILE: labelSelect.cgi
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
	
	#sorting conditionals
	if (cgi['label_sort'] == 'Unordered')
		labelSelect = db.query "SELECT * FROM Label"
	end

	if (cgi['label_sort'] == 'Alphabetical Order')
		labelSelect = db.query "SELECT * FROM Label ORDER BY label_name"
	end

	if (cgi['label_sort'] == 'Ascending Founding Date')
		labelSelect = db.query "SELECT * FROM Label ORDER BY founding_date"
	end

	if (cgi['label_sort'] == 'Descending Founding Date')
		labelSelect = db.query "SELECT * FROM Label ORDER BY founding_date DESC"
	end


	puts "<!DOCTYPE html>"
	puts "<html> <body style='background-color:#ccccff; font-size:20px;'>"
	puts "<table style='border: 1px solid black; border-spacing:8px;'>"
	puts "<title> Labels </title>"
	puts "<p style='text-align:center; font-size:30px;'> LABELS  <br> You might want to scroll down... <br> </p> <tr> <th> LABEL NAME  </th>"
	puts " <th>  LABEL FOUNDING DATE </th> </tr>"

	labelSelect.each do |row|
		puts "<br> <tr>"

		# date datatype must be converted to string if NULL to avoid typeError
		if row['founding_date'].to_s == "NULL"
			row['founding_date'] = "NULL"
		end

		puts "<td> " + row['label_name'] + "</td>" + " " + "<td>" + row['founding_date'].to_s + "</td>"
		puts "<br> </tr>"
	end