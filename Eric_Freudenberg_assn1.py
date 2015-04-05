
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Eric Freudenberg

Assignment 1

Print the value of my_amount without changing it, but only display two decimal places.
The correct output should be 25.68

Then print the next three variables (my_first_number, my_second_number, and 
my_third_number) so that they also only show two decimal places and so that they are 
right-aligned in a column with a width of six characters. The output should look like:
124.54
 51.49
  6.28
"""

my_amount = 25.678437
print "%0.2f" %(my_amount) #I used the formatting sequence for floating point numbers %f to only show 2 decimal points

my_first_number = 124.5392
my_second_number = 51.493333
my_third_number = 6.28345

print "%6.2f" %(my_first_number) #again, I used the %f formatting sequence to only show 2 decimal points and right align with a with of 6. 
print "%6.2f" %(my_second_number)
print "%6.2f" %(my_third_number)