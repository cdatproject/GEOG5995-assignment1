# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Creates Agent class
Defines move() behaviour of Agent
agent's y and x move randomly +-1, torus solution to deal with boundary effects
Protects y and x coordinates using _y and _x
Sets getter, setter and del  of _y and _x with property()

"""

import random

class Agent():
    def __init__(self):
        """
        Initiates Agent class
        
        Agents assigned random (y,x) co ordinates in [0,100]
        Protects y and x coordinates using _y and _x
        Sets getter, setter and del  of _y and _x with property()
        """
        
        self._x = random.randint(0,100)
        self._y = random.randint(0,100)
        
        # Move the agents.
    def move(self):
        """
        Defines move() behaviour of Agent
        agent's y and x move randomly +-1, torus solution to deal with boundary effects
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
            
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
    
    def __str__(self):
        """
        Overwrites __str__ to return x and y coordinate of agent
        """
        return "agent-x: {0}, agent-y: {1}".format(self._x, self._y)

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
