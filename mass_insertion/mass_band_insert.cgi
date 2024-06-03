#!/usr/bin/ruby

require 'cgi'
require 'stringio'
require 'mysql2'

$stdout.sync = true
$stderr.reopen $stdout

print "Content-type: text/html\r\n\r\n"

uploadLocation = "/NFSHome/emora/public_html/songs_db/songsFolder/"
cgi = CGI.new("html5")  # add HTML generation methods

# create a Tempfile reference
fromfile = cgi.params['fileName'].first
originalName = cgi.params['fileName'].first.instance_variable_get("@original_filename")

# create output file reference as original filename in our chosen directory
tofile = uploadLocation + originalName 

# copy the file
# note the untaint prevents a security error
# cgi sets up an StringIO object if file < 10240
# or a Tempfile object following works for both
  
File.open(tofile.untaint, 'w') { |file| file << fromfile.read}

db = Mysql2::Client.new(
	:host=> '10.20.3.4',
	:username=> 'dbms_em',
	:password=> 'em_moorman',
	:database=> 'dbms_em_dbA'
)

allLines = IO.readlines(tofile)

# split strings into seperate fields for table use

allLines.each do |line| 
    field = line.split(",")
    group_name = field[0]
    label_name = field[1]
    group_debut_date = field[2]
    number_of_members = field[3]
	
	labelInsert = db.query("INSERT IGNORE INTO Label(label_name) 
	VALUES('" + label_name + "');")

	bandInsert = db.query("INSERT IGNORE INTO Band(group_name, label_name, group_debut_date, number_of_members)
	VALUES ('" + group_name + "','" + label_name + "','" + group_debut_date + "'," + number_of_members + ");")

end

		
print "<HTML>\n"
print "<HEAD>"
print "<meta http-equiv='refresh' content='20; url=label.html'>"
print "<TITLE>Band Upload Done</TITLE></HEAD>"

print "<body> \n"

#displays success message
print "<H1> Band insert completed! </H1>\n"
print "Uploaded: <br>" + originalName
print "</BODY>\n"
print "</HTML>\n"
