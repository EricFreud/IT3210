
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Eric Freudenberg

Assignment 2

This program should receive input from the user from both the command line arguments
used when launching the script and by use of prompts while the script is running. The
comments in this assignment give further guidance on what specific input is expected
and how it is to be handled.

Feel free to be creative and go beyond the minimum requirements. The primary learning
objective of this assignment is receiving user input, both from command line arguments
and within the program's execution. Can you incorporate any previously learned knowledge
about Python into this exercise?
"""

from sys import argv

script_name, user_name, age = argv 

age = raw_input("How old are you? ") 

print "hi %s, you are at the very YOUNG age of %r years old." %(user_name, age) 

"""
The next two questions ask your height in feet and inches. If you are 5'11",
answer 5 to the first question and 11 to the second.
"""

height_feet = raw_input("How many feet tall are you (excluding inches)? ") 
height_inches = raw_input("How many inches tall are you (excluding feet)? ") 

print "OK %s, you are %r', %r\" tall" % (user_name, height_feet, height_inches) 

inches = (int(height_feet) * 12) + int(height_inches)					# I originally had this in two lines:   x = int(height_feet) * 12 
																		# 										inches = x + int(height_inches)
																		# This way combines it into one line and still does the calculation. 
print "That means, %s, that you are %d inches tall." % (user_name, inches) 