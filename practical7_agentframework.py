# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Creates Agent class
Agents get random (y,x) co ordinates in [0,300], [0,300]
Adds environment and store to constructor function, setting store=0
Defines move(), eat(), distance_between() and share with neighbour() behaviours of Agent
Eats 10 if environment >10, eats remainder if environment<10, sicks up all if store >100
agent's y and x move randomly +-1, torus solution to deal with boundary effects

Overwrites __str__(self) to display coordinates and store

"""


import random


class Agent():
    def __init__(self,environment, agents):
        """
        Initiates Agent class
        
        Agents assigned random (y,x) co ordinates in [0,300]
        Initiates the store attribute with value = 0
        """
        
        self.x = random.randint(0,300)    #change from 300 to check share_with_neighbour
        self.y = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
        
        # Move the agents.
    def move(self):
        """
        Defines move() behaviour of Agent
        
        agent's y and x move randomly +-1, torus solution to deal with boundary effects
        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
    
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
    def eat(self): 
        """
        Agent eats 10 if environment is >10 at (y,x)
        
        or remainder if environment <10
        If store is >100 then agent sicks it up and store reset to 0
        Adds the sick amount back to the environment
        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
# =============================================================================
# At the moment, the agents only eat 10 units at a time. This will leave a
#  few units in each area, even if intensly grazed. This makes them eat
#  the last few bits, if there's less than 10 left, without leaving negative
#  values
#             
# =============================================================================
        else:
            
            self.store += self.environment[self.y][self.x]  
            self.environment[self.y][self.x] = 0
            
            
# =============================================================================
# agents sick up their store in a location if they've 
# been greedy guts and eaten more than 100 units? (note that when you add or
#     subtract from the map, the colours will re-scale). 
# =============================================================================
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    
    
            
    def distance_between(self, neighbour):
        """
        Returns distance between two agents
        """
        return (((self.y - neighbour.y)**2) + 
            ((self.x - neighbour.x)**2))**0.5
        
    
    
    
    def share_with_neighbours(self, neighbourhood):
        """
        Checks distance between each agent using distance_between
        
        Takes "neighbourhood" argument
        Prevents agent checking against itself
        If distance less than neighbourhood:
            The stores are added together and shared equally
        """
        
        #print(neighbourhood)          #testing initial setup
        for agent in self.agents:
            if agent != self:          #prevents agent comparing with itself
                distance = self.distance_between(agent) 
                #print("distance between", self.x, self.y, " : ", 
           #        agent.x, agent.y," : ", distance)        #testing distance function
                if distance <= neighbourhood:
                    average_store = (self.store + agent.store)/2
                    #print("store", self.store, "neighbour store", agent.store)
                    self.store = average_store
                    agent.store = average_store
                    #print("average store: ", average_store)
 # =============================================================================
# override __str__(self) in the agents,  so that they
#  display this information information about their location and stores when printed? 
# =============================================================================
    def __str__(self):
        """
        Overwrites __str__ to return x and y coordinate of agent and store
        """
        return "agent-x: {0}, agent-y: {1}, store-agent: {2}".format(self.x, self.y, self.store)
       