# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Defines distance_between to calculate distance betwen 2 agents.
Import in.txt into environment[] to create agent environment
Set agents dimensions equal to environment dimensions
Creates num_of_agents agents of Agent class using Practical6_agentframework_xy.py module
Agents stored in agents[]
Agents call eat() and move() each iteration
Plots agents final postion after num_of_iterations iterations
Writes environment to environment_eaten.txt after model has run
Appends all agent stores to agents_stores.txt
Appends total amount eaten by all agents to all_agents_stores_total.txt
"""
# =============================================================================
# Practical6 - I/O
# =============================================================================
import matplotlib.pyplot
import practical6_agentframework_xy
import csv

"""
initialise empty agent list and empty environment list

set num_of_iterations, set num_of_agents
"""

num_of_agents = 10
num_of_iterations = 5
agents = []
environment = []


def distance_between(agents_row_a, agents_row_b):
    """
    define distance_between function to calculate distance between 2 agents
    """
    return (((agents_row_a._y - agents_row_b._y)**2) + ((agents_row_a._x - agents_row_b._x)**2))**0.5
#setting up the environment
#in.txt is raster data, with each value being the equivalent to a pixel in an 
#image, arranged in a grid    
"""
open and read in.txt and add to environment
"""
f = open("in.txt", newline="")
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #prevents the float TypeError
""" write environment to environment[]"""
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# =============================================================================
# getting agents to wander around the full environment by finding out 
# the size of environment inside the agents, and using the size when you 
# randomize their starting locations and deal with the boundary conditions? 
# =============================================================================

"""
set y and x dimensions same as environment
"""
x_dimension =  len(environment)
y_dimension =  len(environment[0]) # presuming each list in environment of same length

"""
print envinroment dimensions
"""
print("environment x dimension", len(environment))
print("environment y dimension", len(environment[0]))

"""
generate num_of_agents Agents from agentframework.py

store agents in agents container
add environment and y_dimension and x_dimension to each agent
"""

# Make the agents.
for i in range(num_of_agents):
    agents.append(practical6_agentframework_xy.Agent(environment, 
                                                y_dimension, x_dimension))
  
 # Move the agents.
for j in range(num_of_iterations):
    """
    moves agents num_of_iterations times
    """
    for i in range(num_of_agents):
        """
        agents call eat() after move()
        """
        agents[i].move(x_dimension, y_dimension)
        agents[i].eat()



# =============================================================================
# #testing greedy and grazing until the environment is zero
a = practical6_agentframework_xy.Agent(environment, y_dimension, x_dimension)
print("a: ", a)
print(" a environment", a.environment[a._y][a._x])
print("store a", a.store)
a.store = 200 # set to greater than 100 to check sick code
print("store a", a.store)
print("a: ", a)
environment[a._y][a._x] = 9 # set to <10 to check grazing to 0 code
print("environment a", a.environment[a._y][a._x])
a.eat()
print("environment after eating:",a.environment[a._y][a._x])
print("store a after eating", a.store)
# =============================================================================

"""
plot environment

plot num_of_agents agents after num_of_iterations iterations
"""

# plot the agents final position after eating and moving
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(300, 0)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
    matplotlib.pyplot.scatter(200,0) #test x and y correct way round
matplotlib.pyplot.show()

# =============================================================================
#   Writes out the environment as a file at the end
# =============================================================================
"""
write environment after model has run to environment_eaten.txt
"""
environment_eaten = open("environment_eaten.txt", 'w', newline="")
w = csv.writer(environment_eaten, delimiter=',')
for line in environment:
    w.writerow(line)
#    for value in line:
#        environment_eaten.write(value)
environment_eaten.close()

# =============================================================================
# a second file: agents_stores.txt that writes out the total amount stored by 
# each of the agents on a line. Appends the data to the file, rather than
# clearing it each time it runs. This writes out the store value for each agent
# =============================================================================
"""
append all agent's stores to agent_stores.txt each time model runs
"""
agents_stores = open("agents_stores.txt", 'a', newline="")
agents_store_line = []
for i in range(num_of_agents):
    agents_store_line.append(agents[i].store)
w = csv.writer(agents_stores, delimiter=',')
w.writerow(agents_store_line)
agents_stores.close()


# =============================================================================
# a third file: all_agents_stores_total.txt that writes out the total amount stored by 
# all the agents on a new line. Appends the data to the file, rather than
# clearing it each time it runs. This writes out the total store for all agents
# less lines of code than option used in third file
# =============================================================================
"""
Appends total amount eaten by all agents to all_agents_stores_total.txt each time model is run
"""
store_total = 0
for i in range(num_of_agents):
    store_total = store_total + agents[i].store
f = open("all_agents_stores_total.txt", 'a')
f.write('{}'.format(store_total))
f.write("\n")
f.close() 