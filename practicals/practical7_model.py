# -*- coding: utf-8 -*-
"""
Created on  oct 13 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Import in.txt into environment[] to create agent environment
Sets sys.argv parameters: num_of_iterations, num_of_agents, neighbourhood
Num_of_agents = int(sys.argv[1])
Num_of_iterations  = int(sys.argv[2])
Neighbourhood = int(sys.argv[3])
Exits if incorrect number of parameters entered
Creates num_of_agents agents of Agent class using practical7_agentframework_xy.py module
Agents stored in agents[]
Agents shuffled then call eat() move() and share_with_neighbour() each iteration
Plots agents final postion after num_of_iterations iterations
Writes environment to environment_eaten.txt after model has run
Appends all agent stores to agents_stores.txt
Appends total amount eaten by all agents to all_agents_stores_total.txt
"""

# =============================================================================
# 
# Practical7 - extras  -  Communicating:
# adds in sys.argv parameter definition
# =============================================================================

import matplotlib.pyplot
import practical7_agentframework
import csv
import random # needed for shuffling the agents
import sys #used for argv
#import subprocess #used for subprocess call

#subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
#num_of_agents = 15
#num_of_iterations = 4
"""
initialise empty agent list and empty environment list
"""
agents = []
environment = []
#neighbourhood = 20

"""
set sys.argv arguments and exit if incorrect number entered
"""
sys.argv[0] = "practical7_model.py"
num_of_agents = int(sys.argv[1])
num_of_iterations  = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
count = len(sys.argv[1:])
if count !=3:

   print("Incorrect number of arguments (expecting 3):  exiting")
   exit()
   print("incorrect number of arguments entered. Using default values")
#num_of_agents = 3
#num_of_iterations  = 2
#neighbourhood = 20

#catching exceptions. Won't run if not an integer or not enough arguments

"""
open and read in.txt and add to environment
"""
#setting up the environment
f = open("in.txt", newline="")
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #prevents the float TypeError
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()


# Make the agents.
#getting a link to the list of agents into each agent. 
"""
generate num_of_agents Agents from practical7_agentframework.py

store agents in agents container
"""

for i in range(num_of_agents):
    agents.append(practical7_agentframework.Agent(environment, agents))
 
  
#shuffling prevents artifact error
#testing each agent has list of agents. 
#print(agents[0].agents[1].x) # printing x value of another agent
    
# Move the agents.
"""
randomly shuffles agent order
"""  
for j in range(num_of_iterations):
    #print(agents)       #checking shuffling
    random.shuffle(agents)
    #print(agents)       #checking shuffling
    for i in range(num_of_agents):
        """
        moves agents num_of_iterations times
        
        agents call eat() after move()
        agents call share with neighbour and share stores if distance between<neighbourhood
        """
        agents[i].move()
        agents[i].eat()
        #print("store before sharing, agent: ",i, agents[i].store)
        agents[i].share_with_neighbours(neighbourhood)
        #print("store after, agent:",i, agents[i].store)  #testing share with neighbour
# =============================================================================
# #testing section from practical 5
# a = practical6_agentframework.Agent(environment)
# print("a: ", a)
# print("a.y", a.y, "a.x: ", a.x) 
# a.move()
# print("a.y", a.y, "a.x: ", a.x)
# 
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
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    #matplotlib.pyplot.scatter(200,0) #test x and y correct way round
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

