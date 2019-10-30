# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
magnitudes_of_agents sets different numbers of agents for the model
Makes num_of_agent agents, moves agents num_of_iterations iterations 
and defines distance_between to calculate distance betwen 2 agents.
Agents have (y,x) coordinates
Implements torus solution to deal with boundary effect
Plots the time to run distance_between against different numbers of agents

"""
# =============================================================================
# PRACTICAL 4 - Building tools. in this extra version I plot only the times
#for the model to run against the num_of_agents and not their final positions
# ========================================================================

import random
import operator # only needed if using max function
import matplotlib.pyplot
#import time                
from time import perf_counter # used to time calculations

#number of agents need to be >=2
#num_of_agents = 3 replaced with varying amounts of agents to compare times and
#plot scatter graph
"""
initialise empty agent list, distances list and times_to_plot list,

set num_of_iterations, set num_of_agents, set magnitudes_of_agents
"""
#magnitudes_of_agents sets a range of different number of agents to run
#the model with to allow testing of time taken for different numbers of agents
magnitudes_of_agents = range(2,18,5)
num_of_iterations = 5
agents = []
distances = []        #used to find max and min distances for each iteration
times_to_plot = []    #used store number of agents and time to run for each magnitude of agents


def distance_between(agents_row_a, agents_row_b):
    """
    calculate distance between 2 agents
    """
    length = (((agents_row_a[0] - agents_row_b[0])**2) + 
          ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    
    return(length)
    
"""
run model for each num_of_agents in magnitudes_of_agents

make num_of_agents agents, agent coordinates randomly generated in [0,100] 
"""

for num_of_agents in  magnitudes_of_agents: 
    # Make the agents.
    agents = []
    for i in range(num_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])
    
    # Move the agents.
    for j in range(num_of_iterations):
        """
        randomly move each agent (y,x) coordinates num_of_iterations times +/- 1
        """
        for i in range(num_of_agents):
            """use torus solution to keep agents within 100x100 plot
            """
            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100
    
            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100
    
    
    
    
# =============================================================================     
#this version doesnt plot final agent positions
#     matplotlib.pyplot.ylim(0, 99)
#     matplotlib.pyplot.xlim(0, 99)
#     for i in range(num_of_agents):
#         matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#     matplotlib.pyplot.show() 
# =============================================================================
    """
    print agents list
    """
    print(agents)   # agent coordinates used to check distances below
    
#calculating distance between each agent - j ensures no duplication
# =============================================================================
# #start = time.clock()        #to time this part of code
#  - retired function, gives warning - use perf_counter instead
# =============================================================================
# Start the stopwatch / counter 
    """
    start time
    """
    t1_start = perf_counter()     #starts timer 
    
    for i in range(num_of_agents):
        for j in range(num_of_agents):
            if j > i:
                """
                calculate distance between each agent without duplication
                """
                distance = distance_between(agents[i], agents[j])
                print("distance between",i,"and",j, ":", distance) # use to check results
                distances.append(distance)
    
    #find the maximum and minimum distances between your agents
    """
    print max and min distance bewteen agents
    """
    print("maximum distance: ", max(distances))
    print("minimum distance: ", min(distances))
    # =============================================================================
    #retired function in 3.8 
    #end = time.clock()      #ends timing of distance calculations
    # print("time = " + str(end - start))  
    # =============================================================================
    """
    stop time
    """
    t1_stop = perf_counter()
    elapsed_time = t1_stop-t1_start
    """
    print time for num_of_iterations
    """
    print("Elapsed time during the distance calculations in secs after", 
            num_of_iterations, "iterations: ", elapsed_time, 'secs') 

# =============================================================================
# Try a variety of different orders of magnitude of agent numbers. 
# Record the times in seconds and plot them as a scattergraph 
# =============================================================================
    """
    add time in seconds and num_of_agents to time_to_plot
    """
    times_to_plot.append([num_of_agents,elapsed_time])

"""
print num_of_agents and time for model to run for each magnitude_of_agents
"""
print("(no of agents, time taken for iterations): ", times_to_plot)
max_time = (max(times_to_plot, key=operator.itemgetter(1)))[1] 
min_time = (min(times_to_plot, key=operator.itemgetter(1)))[1]
"""
print max and min time for distance calculation to run
"""
print("maximum time: ", max_time)
print("minimum time: ", min_time)
""" 
maptplotlib plot distance calculation time against num_of_agents
"""
matplotlib.pyplot.ylim(0, magnitudes_of_agents[-1]+1)
matplotlib.pyplot.xlim(min_time, max_time + 0.05)
for i in range(len(times_to_plot)):
#    print("times_to_plot[i][0],times_to_plot[i][1]",(times_to_plot[i][0],times_to_plot[i][1])) to test
    matplotlib.pyplot.scatter(times_to_plot[i][1],times_to_plot[i][0])
matplotlib.pyplot.show() 