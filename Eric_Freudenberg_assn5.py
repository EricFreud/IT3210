#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Eric Freudenberg 

Assignment 5

Things are starting to get a lot more complicated. You may feel overwhelmed! This will be
much worse if you are waiting to try to do all of the exercises and homework in one day.
It is imperative that you spend multiple days per week on course material or you will not 
retain it. Since every week is building on the previous week, you can't afford to have to 
relearn the material every week. It will quickly become unmanageable and you'll be tempted 
to cut corners which will become evident in the exams and final project. Stick with it! 
You can do it - but it will take TIME and DEDICATION!

This week, you've been introduced to Boolean logic, list objects, for and while loops.
You've also learned a little about the concept of recursion through the use of nested 
statements. Working with a bunch of simplistic scripts can get boring after awhile, so 
this week I though it would be fun to write something a little more practical: your very
first zip file dictionary attack password cracker.

With that said, a reminder from the syllabus on ethical behavior is in order: Ethical 
behavior is an absolute expectation in the execution of knowledge and tools gained through 
this class. In some cases students may be exposed to activities and/or knowledge that can 
be used illegally. Such activities will be grounds for failure of the course and potential 
administrative or legal action taken against the student.

Complete this code so that it successfully cracks the zip file entitled
crackmeifyoucan.zip. Use the file common_passwords.txt as your attack dictionary. Once
successful, put the password in the comments and explain what the file is so that I know 
you cracked it!
"""

import sys
import zipfile

def crack(next_password):  #Originally, I did not have next_password as the function variable, which is why my function didn't work. 
	try:
		current_password = next_password.strip()
		print 'Trying password %s' % current_password
		zip.setpassword(current_password)
		zip.extractall()
		print 'The password is %s' % current_password
		sys.exit(0)  
	except Exception:
		print '\tWRONG PASSWORD'

if len(sys.argv) > 1:
    zip_file = sys.argv[1]
    zip = zipfile.ZipFile(zip_file, 'r')
else:
    print "You must start the script with the file name of the zip file you want to " \
          "crack as a command line parameter, e.g. 'python assn5.py crackmeifyoucan.zip'"
    sys.exit(1) 

password_file = open('common_passwords.txt', 'rb')  

next_password = password_file.readline()  
		
for next_password in password_file:   #Originally, I had for 'line' instead of for 'next_password' in the for loop, which is why my loop wasn't iterating through the passwords.
	crack(next_password)
	
zip.close()
password_file.close()





