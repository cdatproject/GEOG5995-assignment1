# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:45:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.

Makes num_of_agent agents, moves agents num_of_iterations iterations 
defines distance_between function to calculate distance betwen 2 agents.
Agents have (y,x) coordinates
Plots agents at final postions
Colours most easterly point red
Implements torus solution to deal with boundary effect
"""
# =============================================================================
# CODE SHRINKING II PRACTICAL
# =============================================================================
# =============================================================================
#Make y,x variables.
#Change y and x based on random numbers.
#Make multiple sets of y's and xs, and make these change randomly as well.
#If using Spyder set IPython console graphics setting to automatic and restart Spyder  
#=============================================================================

import random           #for random.random()
import operator         #to get 2nd coordinate when using max function
import matplotlib.pyplot
"""
initialise empty agent list, set num_of_iterations, set num_of_agents
"""
agents = []
num_of_iterations = 2
num_of_agents = 10

# =============================================================================
#randomised integer starting values for each  pair of value between 0 and 100
#eliminating the need for y0 and x0 variables
# =============================================================================
"""
Create agent list with num_of_agents agents, 

each coordinate a random integer between 0 and 100 inclusive
"""

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
print("agents", agents)



# =============================================================================
# Add in code to print the variables out and test they've been assigned properly
# =============================================================================
"""
print y and x co ordinates of all the agents
"""
for num in range(num_of_agents):
    print("y", num, ": ", agents[num][0], "\nx", num, ": ", agents[num][1])
    
# =============================================================================
# code which will alter xi  and yi randomly and independently for num_of_iterations
# random walk one step per iteration- yo, xo replaced by agents[i][i]
    
#Torus implemented to allow agents leaving the top of the area to come
#in at the bottom, and leaving left, come in on the right,     
# =============================================================================
"""
agents y,x coordinates randomly move +/- 1, for num_of_iterations iterations

torus solution keeps them within 100x100 plot
print each agents position after each iteration 
"""

for num in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random()< 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100 # solving boundary issue
        else:
            agents[i][0] = (agents[i][0] - 1) % 100 # solving boundary issue
        
        
        if random.random()< 0.5:
            agents[i][1] =(agents[i][1] + 1) % 100
        else:
            agents[i][1] =(agents[i][1] - 1) % 100  
 
# =============================================================================
# TO test moving y and x
# =============================================================================
     
        print("After iteration: ",num + 1, ": y", i, ": ",agents[i][0] ,
              "\nAfter iteration: ", num + 1, ": x", i, ": ", agents[i][1])
        
        
    
    
        
        
    
# =============================================================================
# Work out distance between y0,x0 and y1,x1 after num_of_iterations
# =============================================================================



# NOT NEEDED FOR THIS PRACTICAL=============================================================================
# distance_between = pow(pow((agents[1][0]-agents[0][0]),2)
#  + pow ((agents[1][1]-agents[0][1]),2),0.5)
# 
# #Testing distance between
# 
# 
# print("(y0,x0): ", agents[0][0], agents[0][1])
# print("(y1,x1): ", agents[1][0], agents[1][1])
# print("Distance between (", agents[0][0], ",", 
#                          agents[0][1], ") and (", agents[1][0], ",",
#                          agents[1][1], "): ", distance_between)
# =============================================================================

# =============================================================================
# work out which agent is furthest east 
# =============================================================================
"""
calculate most easterly point
"""
most_easterly = (max(agents, key=operator.itemgetter(1))) 
print("most easterly: ", max(agents, key=operator.itemgetter(1))) 
 
#plot all the agents after all iterations
"""
plot num_of_agents agents
"""
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
  
#colour most easterly point red
"""
colour most easterly point red
"""
matplotlib.pyplot.scatter(most_easterly[1], most_easterly[0], color='red')
matplotlib.pyplot.show()