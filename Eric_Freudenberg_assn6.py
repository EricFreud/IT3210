"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Eric Freudenberg

Assignment 6

"""

def get_score():  					
	global score 
	score = raw_input("Enter score (type 'end' when finished): ")   				# I added a user friendly Sentence which I didn't have 

def letter_grade(grade):  			
	if grade < 101 and grade > 89:	
		return 'A'
	if grade < 90 and grade > 79:
		return 'B'
	if grade < 80 and grade > 69:           
		return 'C'
	if grade < 70 and grade > 59:
		return 'D'
	if grade < 60:
		return 'F'
	else: 
		print "error"																# I added an error message for invalid entries 

score_list = [] 					 
grade_list = []

student_dict = {
	"Eric Freudenberg": 100,														# I made my dict a little more readable 
	"Jason Rowen": 90, 
	"Jessica Townsend": 88, 
	"Thomas Pane": 74,
	"Max Powell": 62
}										

def print_list():     
	score_list.sort()  
	grade_list.reverse() 
	print "Score", "%8s" % "Grade"   
	print "-" * 5, "%8s" % ("-" * 5)  
	for x, y in zip(score_list, grade_list):  
		print "%5r" % x, "%9r" % y
	print "the lowest score was %r, which is a %r." % (min(score_list), max(grade_list)) 		
	
def print_dict():  					
	for key, val in student_dict.iteritems():  
		grade = val 
		print "%r, your score is %r, which is a %r." %(key, grade, letter_grade(grade))		#I got rid of the "hello", it was kind of annoying 
		
while True:  					
	get_score()
	if score == "end": 
		print_list() 
		print_dict()
		break
	else: 
		grade = int(score)   
		score_list.append(grade)  
		grade_list.append(letter_grade(grade)) 
		  
		
		
		
		
	
