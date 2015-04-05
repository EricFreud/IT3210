#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Eric Freudenberg

Assignment 3

This program should receive two filenames from the user from the command line arguments
used when launching the script, and copy the first file into the second. Use the file
provided (infile.txt) as the input_file.
"""

from sys import argv
from os.path import exists 

input_file, output_file = argv[1:3] 				# This is just an easier way to get the file names using the slice operators. 
													# This is how I originally had it :    script, input_file, output_file = argv 
																						 # t = argv [1:] 
																						 # print t   
# print the absolute path of each file using the relevant function from the os.path module
print 'The absolute path of the input file is %s' % abspath(input_file)
print 'The absolute path of the input file is %s' % abspath(output_file)		#these two lines I didn't have in the original file. 

in_file = open(input_file); indata = in_file.read()								# I did not think this is what was being asked when I was working on the assignment. 
																				#this is what I had: with open(input_file) as f: 
																				#					 indata = f.read()      

print "The input file is %d bytes long" % len(indata)  

print "Does the output file exist? %r" % exists(output_file) 
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(output_file, 'w')
out_file.write(indata)   
           
in_file.seek(0)								# This I didn't have in the original file. Seek allows you to go to the beginning of the file 

print 'The first 13 characters of the input file are %s' % in_file.read(13)		#I didn't have this in a print statement and I wrote it differently. 
																				# Originally I wrote this: with open(input_file) as f:
																										 # indata = f.read(13)        
																										 # print indata

footer = '\n The End'

with open(output_file, "a") as out_file:   # I wrote this a little differently then the solution but it was essentially the same thing so I'm not going to change it. 
    out_file.write(footer)                 

out_file.close()   
f.close()

