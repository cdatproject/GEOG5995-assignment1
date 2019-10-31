# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Creates Agent class
Defines move() and eat() behaviours of Agent
agent's y and x move randomly +-1, torus solution to deal with boundary effects
Protects y and x coordinates using _y and _x
Sets getter, setter and del  of _y and _x with property()
Overwrites __str__(self) to display coordinates and store
"""

import random

#note as this makes agents sick after their store is above 100,
#this will never eat all of the environment unless there are enough agents

class Agent():
    def __init__(self,environment, y_dimension, x_dimension): # adds in environment dimensions
        """
        Initiates Agent class
        
        Agents assigned random (y,x) co ordinates in [0,dimension]
        Requires y_dimension and x_dimension arguments
        Initiates the store attribute with value = 0
        Protects y and x coordinates using _y and _x
        Sets getter, setter and del  of _y and _x with property()
        """
        self._x = random.randint(0,x_dimension)
        self._y = random.randint(0,y_dimension)
        self.environment = environment
        self.store = 0 # set to 100 to check sick code
        
# =============================================================================
# Can you get the agents to wander around the full environment by finding out 
# the size of environment inside the agents, and using the size when you 
# randomize their starting locations and deal with the boundary conditions? 
# =============================================================================
        
        
        
        
        # Move the agents. edited for boundaries of full environment
    def move(self, y_dimension, x_dimension):
        """
        Defines move() behaviour of Agent
        agent's y and x move randomly +-1, torus solution to deal with boundary effects
        """
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % y_dimension
        else:
            self._y = (self._y - 1) % y_dimension
    
        if random.random() < 0.5:
            self._x = (self._x + 1) % x_dimension
        else:
            self._x = (self._x - 1) % x_dimension
            
    def eat(self): # agents eating what is left (>10)
        """
        Agent eats 10 if environment is >10 at (y,x)
        
        or remainder if environment <10
        If store is >100 then agent sicks it up and store reset to 0
        Adds the sick amount back to the environment
        """
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
       
# =============================================================================
# At the moment, the agents only eat 10 units at a time. This will leave a
#  few units in each area, even if intensly grazed. This makes them eat
#  the last few bits, if there's less than 10 left, without leaving negative
#  values
#             
# =============================================================================
        else:
            
            self.store += self.environment[self._y][self._x]  
            self.environment[self._y][self._x] = 0
            
            
# =============================================================================
# agents sick up their store in a location if they've 
# been greedy guts and eaten more than 100 units? (note that when you add or
#     subtract from the map, the colours will re-scale). 
# =============================================================================
        if self.store > 100:
            self.environment[self._y][self._x] += self.store
            self.store = 0
    
    
    
# =============================================================================
# override __str__(self) in the agents,  so that they
#  display this information information about their location and stores when printed? 
# =============================================================================
    def __str__(self):
        """
        Overwrites __str__ to return x and y coordinate of agent and store
        """
        return "agent-x: {0}, agent-y: {1}, agent-store: {2}".format(self._x, self._y, self.store)

    def getx(self):
#        return self._x +1000     #used to test it is calling getx in a.x
        return self._x
        
    def gety(self):
#        return self._y +1000     #used to test it is calling getx in a.x
        return self._y
   
    def setx(self, value):
        self._x = self._x       #stopping x changes in a.x = value
        value = value
        print("called setx")    #testing setx
        print(value+500)
        print(self._x)
        
    def sety(self, value):
        self._y = self._y       #stopping x changes in a.x = value
        value = value
        print("called sety")    #testing setx
        print(value+500)
        print(self._y)   
        
        

    def delx(self):
        del self._x
        
    def dely(self):
        del self._y    
    
    

    x = property(getx, setx, delx, "I'm the 'x' property.")
    y = property(gety, sety, dely, "I'm the 'y' property.")
    
# =============================================================================
# info for setting up property method
#built-in property() method. In Python, 
#  the main purpose of property() function is to create property of a class
# =============================================================================
# Syntax— property(fget=None, fset=None, fdel=None, doc=None)
# 
# Parameters:
# 
# fget() – used to get the value of attribute
# fset() – used to set the value of atrribute
# fdel() – used to delete the attribute value
# doc() – string that contains the documentation (docstring) for the attribute
# Return: Returns a property attribute from the given getter, setter and deleter.
# 
# Note—
# 
# As seen from the implementation, these function arguments are optional.
# If no arguments are given, property() method returns a base property
#  attribute
#  that doesn’t contain any getter, setter or deleter.
# 
# # =============================================================================
# 
# =============================================================================
