# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Creates num_of_agents agents of Agent class using practical5_agentframework_xy.py module
agents stored in agents[]
moves agents num_of_iterations iterations 
Defines distance_between to calculate distance betwen 2 agents.
plots agents final postion after num_of_iterations iterations

"""
# ============================================================================= 
# Practical5 - Agents

#protects the self.x and self.y variables by renaming them self._x and self._y 
#implements a property attribute for them, with set and get methods
# 
# =============================================================================

import matplotlib.pyplot
import practical5_agentframework_xy
#from time import perf_counter # used to time calculations


"""
initialise empty agent list

set num_of_iterations, set num_of_agents
"""

num_of_agents = 10
num_of_iterations = 100
agents = []
#distances = []        #used to find max and min distances for each iteration
#times_to_plot = []    #used store number of agents and time to run for each magnitude of agents


def distance_between(agents_row_a, agents_row_b):
    """
    define distance_between function to calculate distance between 2 agents
    """
    return (((agents_row_a._y - agents_row_b._y)**2) + 
        ((agents_row_a._x - agents_row_b._x)**2))**0.5

#testing section to check effect of set and get in property() in Agent class
"""
print agent a's y and x using _y and _x
"""
a = practical5_agentframework_xy.Agent()
print("a: ", a)

print("a._y", a._y, "a._x: ", a._x) 
print("a._y", a._y, "a._x: ", a._x) #checked x & y set and not regenerated
"""
move agent a once and print y and x using _y and _x
"""
a.move()
print("a.y", a._y, "a._x: ", a._x)

"""
generate num_of_agents Agents from agentframework.py

store agents in agents container
moves agents num_of_iterations times
"""

# Make the agents.
for i in range(num_of_agents):
    agents.append(practical5_agentframework_xy.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
"""
plot num_of_agents agents after num_of_iterations iterations
"""
# plot the agents final position
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x)
matplotlib.pyplot.show()

# =============================================================================
#not used inthis practical# 
#for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b) 
# ============================================================================
 

