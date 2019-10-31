# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:24:49 2019

@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
Creates Agent and Wolf classes.
Both have (y,x) coordinates in the 300x300 environment imported from the raster data in.txt
Agent class
agent's  _y and _x scraped from web data in [0,100], else assigned in [0,300] if data missing
Defines move() and eat(), distance_between(), share with neighbours() methods of Agent
Eats 10 if environment >10, eats remainder if environment<10
Agent's y and x move randomly +-1, torus solution to deal with boundary effects
Overwrites __str__(self) to display coordinates and store
In Wolf class:
Randomly assigned (y,x) co ordinates, y in [0,100], x in [0,300]
Defines chase() and traverse()
Wolf deletes agent if y and x coordinates <10 units apart and sheep_eaten <3
Overwrites __str__(self) to display coordinates and sheep_eaten
Both classes protect y and x coordinates using _y and _x
Sets getter, setter and del  of _y and _x with property()
"""

import random

class Agent():
    def __init__(self,environment, agents,_y= None ,_x = None):#doesnt need _y and _x setting if generating random values below
        """
        Initialises an Agent object
        
        _y, _x from web scraping passed into constructor function
        agent gets copy of the environment
        agent gets copy of list of all other agents
        sets (y,x) randomly in [0,300] if(y,x) arguments missing
        store attribute set to 0
        """ 
        #self._x = random.randint(0,10)    #changed from 300 to check share_with_neighbour
        #self._y = random.randint(0,10)    
        if (_x == None):
            self._x = random.randint(0,300)#use this without if loop to generate random numbers rather than scrape
        else:
            self._x = _x
        
        if (_y == None):
            self._y = random.randint(0,300)#use this without if loop to generate random numbers rather than scrape
        else:
            self._y = _y
        
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
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300
    
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
    def eat(self):
        """
        Agent eats 10 if environment is >10 at (y,x)
        
        or remainder if environment <10. Amount eaten is added to store
        """
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]  
            self.environment[self.y][self.x] = 0
# =============================================================================
# # =============================================================================
# # agents sick up their store in a location if they've 
# # been greedy guts and eaten more than 100 units? (note that when you add or
# #     subtract from the map, the colours will re-scale). 
# # =============================================================================
#         if self.store > 100:
#             self.environment[self._y][self._x] += self.store
#             self.store = 0
# =============================================================================
        
    def distance_between(self, neighbour):
        """
        Returns distance between two agents
        """
        return (((self._y - neighbour._y)**2) + 
            ((self._x - neighbour._x)**2))**0.5
        
    def share_with_neighbours(self, neighbourhood):
        #print(neighbourhood)          #testing initial setup
        """
        Checks distance between each agent using distance_between
        
        Takes "neighbourhood" argument
        Prevents agent checking against itself
        If distance less than neighbourhood:
        The stores are added together and shared equally between the 2 agents
        """
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent) 
                #print("distance between", self._x, self._y, " : ", 
           #        agent._x, agent._y," : ", distance)        #testing distance function
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
        Overwrites __str__ to return _x and _y coordinate of agent and store
        """
        return "agent-_x: {0}, agent-_y: {1}, store-agent: {2}".format(self._x, self._y, self.store)
     
    def getx(self):
        print("Getting x value")
#        return self._x +1000     #used to test it is calling getx in a.x
        return self._x
        
    def gety(self):
        print("Getting y value")
#        return self._y +1000     #used to test it is calling getx in a.x
        return self._y
   
    def setx(self, value):
        print("Setting x value to " + value)
        self._x = value

#        self._x = self._x       #stopping _x changes in a._x = value
#        value = value
#        print("called setx")    #testing setx
#        print(value+500)
#        print(self._x)
        
    def sety(self, value):
        print("Setting y value to " + value)
        self._y = value
#        self._y = self._y       #stopping _y changes in a._y = value
#        value = value
#        print("called sety")    #testing set_y
#        print(value+500)
#        print(self._y)   
        
        

    def delx(self):
        print("Deleting x value")
        del self._x
        
    def dely(self):
        print("Deleting y value")
        del self._y    
    
    

    x = property(getx, setx, delx, "I'm the 'x' property.")
    y = property(gety, sety, dely, "I'm the 'y' property.")


                              
class Wolf():
    """
    list of sheep passed into wolf
    
    wolf given random coordinates, y in [0,100] and x in [0,300]
    sheep_eaten attribute set to 0
    """
    def __init__(self, sheep):
        self._x = random.randint(0,300)
        self._y = random.randint(0,100)
        #self._x = 50
        #self._y = 50
        self.sheep = sheep
        self.sheep_eaten = 0
        
     
    def traverse(self):
        """
        wolf randomly traverses +/-3 along x axis direction 
        """
        if random.random() < 0.5:
            self._x = (self._x + 3) % 300
        else:
            self._x = (self._x - 3) % 300
                
    def chase(self, num_of_sheep, sheep, total_sheep_eaten):
        """
        If wolf is closer than 10 units in x and y direction
        
        and the wolf has eaten less than 3 sheep in the 24 iteration
        period, the wolf moves to the agent (y,x) position
        and deletes (eats) the agent.
        Prints number of sheep left and total sheep eaten
        """
                
        for sheep_i in sheep:
                
                if abs(sheep_i._x - self._x)< 10 and abs(sheep_i._y - self._y) < 10:
                    #print("before eating, total sheep eaten: ", total_sheep_eaten)
                    if self.sheep_eaten < 3:
                        print("wolf eats sheep")
                        print("wolf(y,x): ", self._y, self._x)
                        self._y = sheep_i._y
                        self._x = sheep_i._x
                        sheep.remove(sheep_i)
                        print("sheep(y,x): ", sheep_i._y, sheep_i._x)
                        
                        print("Number of sheep left: ",len(sheep))
                        total_sheep_eaten[0] +=1
                        self.sheep_eaten +=1
                        
                        print("total sheep eaten: ", total_sheep_eaten)
    
# =============================================================================
# override __str__(self) in the agents,  so that they
#  display this information information about their location and sheep eaten 
# =============================================================================
    def __str__(self):
        return "wolf-_x: {0}, wolf-_y: {1}, sheep_eaten: {2}".format(self._x, self._y, self.sheep_eaten)
            
    def getx(self):
        print("Getting x value")
#        return self._x +1000     #used to test it is calling getx in a.x
        return self._x
        
    def gety(self):
        print("Getting y value")
#        return self._y +1000     #used to test it is calling getx in a.x
        return self._y
   
    def setx(self, value):
        print("Setting value to " + value)
        self._x = value
#        self._x = self._x       #stopping x changes in a.x = value
#        value = value
#        print("called setx")    #testing setx
#        print(value+500)
#       print(self._x)
        
    def sety(self, value):
        print("Setting y value to " + value)
        self._y = value
#       self._y = self._y       #stopping y changes in a.y = value
#       value = value
#       print("called sety")    #testing setx
#       print(value+500)
#       print(self._y)   
                
    def delx(self):
        print("Deleting x value")
        del self._x
        
    def dely(self):
        print("Deleting y value")
        del self._y    
    
    x = property(getx, setx, delx, "I'm the 'x' property.")
    y = property(gety, sety, dely, "I'm the 'y' property.")