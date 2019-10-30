# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:45:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.

Makes num_of_agent agents, moves 2 agents num_of_iterations iterations 
and defines distance_between to calculate distance betwen 2 agents.
Agents have (y,x) coordinates
Plots 2 agents at final postions
Colours most easterly point red
"""

# =============================================================================
# PRACTICAL 2:  CODE SHRINKING I 
# =============================================================================
# =============================================================================
# Make a y variable.
# Make an x variable.
# Change y and x based on random numbers.
# Make multiple sets of y and xs, and make these change randomly as well.
# If using Spyder set IPython console graphics setting to automatic and restart Spyder 
#=============================================================================
import random           #for random.random()
import operator         #to get 2nd coordinate when using max function
import matplotlib.pyplot
"""
initialise empty agent list, set num_of_iterations, set num_of_agents
"""
agents = []
num_of_iterations = 3
num_of_agents = 2 # this needs to be 2 as only 2 agents are moved and plotted by this version of code

# =============================================================================
# randomised integer starting values for each  pair of value between 0 and 99
#eliminating the need for y0 and x0
# =============================================================================
"""
Create agent list with num_of_agents agents, 

each coordinate a random integer between 0 and 99 inclusive
"""

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print("agents", agents) #test agents created correctly

# =============================================================================
# Add in code to print the variables out and test they've been assigned properly
# =============================================================================

"""
print yo,xo and y1,x1 coordinates
"""
print("y0: ", agents[0][0], "\nx0: ", agents[0][1])
print("y1: ", agents[1][0], "\nx1: ", agents[1][1])
# =============================================================================
# code which will alter xi  and yi randomly and independently
# random walk one step - then updated to walk a number of iterations.
# yo, xo replaced by agents[i][i]
# =============================================================================
"""
yo,xo coordinates move randomly + or -1 for i num_of_iterations iterations

print yo,xo new co ordinates after each iteration i
""" 

for i in range(num_of_iterations):

    if random.random()< 0.5:
        agents[0][0] +=  1
    else:
        agents[0][0] -=  1
    
    
    if random.random()< 0.5:
        agents[0][1] +=  1
    else:
        agents[0][1] -=  1  
        
    
# =============================================================================
# To test altering y0 and x0
# =============================================================================

    print("After iteration: ",i, "y0: ",agents[0][0] ,
          "\nAfter iteration: ", i, "x0: ", agents[0][1])
    
    
# =============================================================================
# making second agent y1 x1 move randomly for num_of_iterations
# =============================================================================
"""
y1,x1 coordinates move randomly + or -1 for i num_of_iterations iterations

print yo,xo new co ordinates after each iteration i
""" 

for i in range(num_of_iterations):

    if random.random()< 0.5:
        agents[1][0] +=  1
    else:
        agents[1][0] -=  1
    
    
    if random.random()< 0.5:
        agents[1][1] +=  1
    else:
        agents[1][1] -=  1  
        
    
# =============================================================================
# To test altering y1 and x1
# =============================================================================
    
    print("After iteration: ",i, "y1: ",agents[1][0] , 
          "\nAfter iteration: ", i, "x1: ", agents[1][1])
    
    
# =============================================================================
# Work out distance between y0,x0 and y1,x1 after num_of_iterations
# =============================================================================

"""
calculate distance between y1,x1 and y0,x0
"""
distance_between = pow(pow((agents[1][0]-agents[0][0]),2)
 + pow ((agents[1][1]-agents[0][1]),2),0.5)

#Testing distance between

"""
print distance between y1,x1 and y0,x0
"""
print("(y0,x0): ", agents[0][0], agents[0][1])
print("(y1,x1): ", agents[1][0], agents[1][1])
print("Distance between (", agents[0][0], ",", 
                         agents[0][1], ") and (", agents[1][0], ",",
                         agents[1][1], "): ", distance_between)

# =============================================================================
# work out which agent is furthest east 
# =============================================================================
"""
calculate most easterly point
"""
most_easterly = (max(agents, key=operator.itemgetter(1))) 
print("most easterly: ", max(agents, key=operator.itemgetter(1))) 
 
#plot the agents after all iterations using matplotlib
"""
plot 2 agents and colour most easterly point red
"""
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#colour most easterly point red
matplotlib.pyplot.scatter(most_easterly[1], most_easterly[0], color='red')
matplotlib.pyplot.show()