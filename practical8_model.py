# -*- coding: utf-8 -*-
"""
Created on  oct 13 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Sets num_of_agents, num_of_agents, neighbourhood, carry_on
Creates matplotlib figure
Import in.txt into environment[] to create agent environment
Creates num_of_agents agents of Agent class using practical8_agentframework.py module
Agents stored in agents[]
Defines update() for animation
Agents call eat() move() and share_with_neighbour() each iteration within update() and checks carry_on condition
defines generator function gen_function() to use as frames argument in FuncAnimation
gen_function() uses 2 stopping conditions - carry_on and num_of_iterations
carry_on set to false when all sheep have eaten at least 300
Plots agents final postion after each iteration in figure1 animation
"""
# =============================================================================
# 
# Practical8 - Animation and Extras
# 
# =============================================================================
import matplotlib.pyplot
import practical8_agentframework
import csv
import random # needed for shuffling the agents
import matplotlib.animation #for animation practical

"""
initialise empty agent list and empty environment list

set num_of_agents, num_of_iterations, carry_on stopping condition
"""

num_of_agents = 5
num_of_iterations = 10
agents = []
environment = []
neighbourhood = 20
carry_on = True	 #used for stopping condition

"""
create matplotlib figure
"""
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#setting up the environment
"""
open and read in.txt and add to environment
"""
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
generate num_of_agents Agents from practical8_agentframework.py

store agents in agents container
"""

for i in range(num_of_agents):
    agents.append(practical8_agentframework.Agent(environment, agents))


#for setting up animation
def update(frame_number):
    """
    Define update function for animation display
    """
    fig.clear()   
    global carry_on # stopping condition
#testing each agent has list of agents. 
#print(agents[0].agents[1].x) # printing x value of another agent
    
 # Move the agents.
    for j in range(num_of_iterations):
        """
        randomly shuffles agent order
        """
        print(agents)       #checking shuffling
        random.shuffle(agents)
        print(agents)       #checking shuffling
        for i in range(num_of_agents):
            """
            Moves agents num_of_iterations times
            
            Agents call eat() after move(). Eats, 10, empties environment if <10 or sicks up all if store>100
            Agents call share_with_neighbour and share stores if distance between<neighbourhood
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


#stopping condition
        for i in range(num_of_agents):
            """
            Check stopping condition when all sheep have eaten 300
            """
            sheep_full = 0
            if agents[i].store >= 300:     #stops when all sheep have eaten at least 90
                sheep_full += 1
            if sheep_full == num_of_agents:    
                carry_on = False
                print("stopping condition")

    
# plot the agents final position after eating and moving
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(300, 0)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    #matplotlib.pyplot.scatter(200,0) #test x and y correct way round


"""define gen_function() to use 2 stopping conditions"""
def gen_function(b = [0]): # limits code to not running more than num_of_iterations
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1



"""
runs animation plotting agents after each iteration
"""
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,
                                        repeat=False, frames=gen_function)
matplotlib.pyplot.show()
"""
Animation plots until stopping condition met
"""
# =============================================================================
# # =============================================================================
# #   Writes out the environment as a file at the end
# # =============================================================================
# """write environment after model has run to environment_eaten.txt"""
# environment_eaten = open("environment_eaten.txt", 'w', newline="")
# w = csv.writer(environment_eaten, delimiter=',')
# for line in environment:
#     w.writerow(line)
# #    for value in line:
# #        environment_eaten.write(value)
# environment_eaten.close()
# 
# # =============================================================================
# # a second file: agents_stores.txt that writes out the total amount stored by 
# # each of the agents on a line. Appends the data to the file, rather than
# # clearing it each time it runs. This writes out the store value for each agent
# # =============================================================================
# """append all agent's stores to agent_stores.txt each time model runs"""
# agents_stores = open("agents_stores.txt", 'a', newline="")
# agents_store_line = []
# for i in range(num_of_agents):
#     agents_store_line.append(agents[i].store)
# w = csv.writer(agents_stores, delimiter=',')
# w.writerow(agents_store_line)
# agents_stores.close()
# 
# 
# # =============================================================================
# # a third file: all_agents_stores_total.txt that writes out the total amount stored by 
# # all the agents on a new line. Appends the data to the file, rather than
# # clearing it each time it runs. This writes out the total store for all agents
# # less lines of code than option used in third file
# # =============================================================================
# """Appends total amount eaten by all agents to all_agents_stores_total.txt each time model is run"""
# store_total = 0
# for i in range(num_of_agents):
#     store_total = store_total + agents[i].store
# f = open("all_agents_stores_total.txt", 'a')
# f.write('{}'.format(store_total))
# f.write("\n")
# f.close() 
# 
# 
# 
# =============================================================================
