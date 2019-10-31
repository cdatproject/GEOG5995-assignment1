# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:45:49 2019

@author: liz
This file is covered by the LICENSING file in the root of this project.

Makes 2 agents, moves them and defines distance_between to 
calculate distance betwen 2 agents

"""

# =============================================================================
# AGENT BASED MODELLING PRACTICAL
# =============================================================================
# =============================================================================
#  Make a y variable.
#  Make an x variable.
#  Change y and x based on random numbers.
#  Make a second set of y and xs, and make these change randomly as well.
#  Work out the distance between the two sets of y and xs.
# =============================================================================

import random           #for random.random()


# =============================================================================
# make two variable labels, "y0" and "x0" and assign them the values 50 and 50.
#then add in 2nd variable labels y1 x1 also both with value 50
# =============================================================================


"""
make four variable labels, "y0","x0","y1","x1" 
""" 

# =============================================================================
#removed to replace with randomised integer starting values between 0 and 99
# y0 = 50
# x0 = 50
# y1 = 50
# x1 = 50
# =============================================================================
y0 = random.randint(0,99)
x0 = random.randint(0,99)
y1 = random.randint(0,99)
x1 = random.randint(0,99)
"""
set number of iterations 
"""
num_of_iterations = 3


# =============================================================================
# Add in code to print the variables out and test they've been assigned properly
# =============================================================================
""" 
print variables to test they've been assigned properly
"""
print("y0: ", y0, "\nx0: ", x0)
print("y1: ", y1, "\nx1: ", x1)
# =============================================================================
# code which will alter x0  and y0 randomly and independently
# random walk one step - updated to number of iterations
# =============================================================================

""" 
randomly adds or deletes 1 from y0 and x0 

print y0 x0 after each iteration i 
""" 

for i in range(num_of_iterations):

    if random.random()< 0.5:
        y0 +=  1
    else:
        y0 -=  1
    
    
    if random.random()< 0.5:
        x0 +=  1
    else:
        x0 -=  1  
        
    
# =============================================================================
# test altering y0 and x0
# =============================================================================

  
    print("After iteration: ",i, "y0: ",y0 , "\nAfter iteration: ", i, "x0: ", x0)
    
    
# =============================================================================
# making second set of points to represent the position of a second agent y1, x1
# =============================================================================
""" 
randomly adds or deletes 1 from y0 and x0 

print y0 x0 after each iteration i 
""" 

for i in range(num_of_iterations):

    if random.random()< 0.5:
        y1 +=  1
    else:
        y1 -=  1
    
    
    if random.random()< 0.5:
        x1 +=  1
    else:
        x1 -=  1  
        
    
# =============================================================================
# TO test altering y0 and x0
# =============================================================================
    
    print("After iteration: ",i, "y1: ",y1 , "\nAfter iteration: ", i, "x1: ", x1)
    
    
# =============================================================================
# Work out distance between y0,x0 and y1,x1 after num_of_iterations
# =============================================================================

# =============================================================================
# code to test distance between - this should produce answer = 5
# y0 = 0
# x0 = 0
# y1 = 4
# x1 = 3
# =============================================================================


""" 
work out distance between 2 points (y0,x0) and (y1,x1) 
"""
distance_between = pow(pow((y1-y0),2) + pow ((x1-x0),2),0.5)

#Testing distance between
"""
print distance_between result for (y0,x0) and (y1, x1) 
"""
print("(y0,x0): ", y0, x0)
print("(y1,x1): ", y1, x1)
print("Distance between (", y0, ",", x0, ") and (", y1, ",", x1, "): ", distance_between)