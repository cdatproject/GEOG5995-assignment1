# -*- coding: utf-8 -*-
"""__version__  1.0.0

Created on  oct 13 17:24:49 2019
@author: Liz Osbourn
This file is covered by the LICENSING file in the root of this project.
This runs in a GUI and opens 2 windows ("Figure 1" and "Sheep").
Both windows must be left open. 
In the "Sheep" window select "Run model" from the "Model" dropdown menu to run the model. 
sys.argv Variables to set are num_of_agents, num_of_iterations, neighbourhood
Imports in.txt into environment[] to create agent environment
Creates num_of_agents agents of Agent class using sheep_wolf_agentframework.py module
agent y, x coordinates are scraped from data.html and are in [0,100]
Agents stored in agents[]
Defines update() for animation display
Wolves chase() - deleting agents closer than 10 units if they have eaten less than 3 in the 24 iteration period
wolf position plotted with X then wolves traverse()
Agents call eat() move() and share_with_neighbours() each iteration within update() and checks carry_on condition
Defines generator function gen_function() to use as frames argument in FuncAnimation
Gen_function() uses 2 stopping conditions - carry_on and num_of_iterations
Carry_on set to false when all agent's stores = full_belly
Plots agents final postion after each iteration in figure1 animation
Select "END" from the "Model" dropdown menu to close the GUI
Environment written out to environment_eaten.txt at the end
Agents store totals appended on one line to agents_stores.txt
Model data written to model_data.txt
"""
# =============================================================================
# 
# Practical9 - Gui/web scraping
# 
# =============================================================================
"""
import matplotlib, matplotlib.pyplot, tkinter,csv, random, matplotlib.animation, requests, bs4 modules
"""

import matplotlib
matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import (
    #FigureCanvasTkAgg) # put in whilst testing different code
import matplotlib.pyplot
import tkinter
from tkinter import messagebox
#import os #only needed for os.exit(1) in finish()
import sheep_wolf_agentframework
import csv
import random # needed for shuffling the agents
import matplotlib.animation #for animation practical
import requests
import bs4
from datetime import datetime # datetime object containing current date and time
import sys 
"""
set sys.argv arguments and exit if incorrect number entered
"""
sys.argv[0] = "sheep_wolf__modelargtest.py"
num_of_agents = int(sys.argv[1])
num_of_iterations  = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
count = len(sys.argv[1:])
if count !=3:

   print("Incorrect number of arguments (expecting 3):  exiting")
   exit()
   print("incorrect number of arguments entered. Using default values")


#catching exceptions. Won't run if not an integer or not enough arguments

# not used if running from command line=============================================================================
# """
# set number of agents
# 
# set number of iterations
# set neighbourhood
# """
# =============================================================================
"""
Create empty agent container

Create empty environment container
initalise stopping condition
Create empty wolf container
Set number of wolves
Set total_sheep_eaten to 0
set hour count to 0
set sheep_full to 0
set full_belly
"""

#num_of_agents = 5
#num_of_iterations = 5
agents = []
environment = []
#neighbourhood = 20
global carry_on	 #used for stopping condition
carry_on = True
wolves = []
#no_of_wolves = 1 #use if want to keep wolves constant for testing
no_of_wolves = random.randint(0,(round(num_of_agents/5)+1))
total_sheep_eaten = [0]
hour_count = 0 # used for resetting wolves hunger every 24 iterations
#global sheep_full
sheep_full=0  #used to determine value of carry_on stopping condition
full_belly=300 # used to determine value of carry_on stopping condition
"""
Set up the environment using in.txt
"""
#setting up the environment using in.txt
#in.txt contains raster data for a 300x300 grid
f = open("in.txt", newline="")
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #prevents the float TypeError
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# =============================================================================
# This builds the main window ("root"); sets its title
# =============================================================================

root = tkinter.Tk() 
root.wm_title("Sheep")
#data.html only contains y and x in [0,100] so to get full
#coverage of environment can use random.randint() technique from previous
#practicals to generate (y,x) coordinates and comment out the below section
"""
Scrape data.html to obtain y,x coordinates
"""
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) - used for checking code
#print(td_xs) - used for checking code


#Make the agents.
#getting a link to the list of agents into each agent. 
#pass x and y from data.html into agents 
"""
Populate agent container with agents with(y,x) values scraped from data.html
""" 
for i in range(num_of_agents):
    #agents.append(practical9_agentframework.Agent(environment, agents))
    _y = int(td_ys[i%100].text)#remove these 2 lines and _y,_x from line below 
    _x = int(td_xs[i%100].text)#to use random (_y,_x) in Agent class
    agents.append(sheep_wolf_agentframework.Agent(environment, agents, _y, _x))
#if i is greater than length of td_ys (100) would get an error without %100
"""
create wolves
"""
for i in range(no_of_wolves):
    wolves.append(sheep_wolf_agentframework.Wolf(agents))

# =============================================================================
# # lays out a matplotlib canvas embedded within our window and associated
# #  with fig, our matplotlib figure. 
# =============================================================================


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#for setting up animation
def update(frame_number):
    """
    Updates the display in the animation
    
    Adds 1 to hour_count
    """     
    fig.clear()   
    global carry_on 
    global hour_count
    global sheep_full # global to enable printout to file at end
    hour_count+=1
    sheep_full = 0
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(300, 0)
    matplotlib.pyplot.imshow(environment)
 # Move the agents.
    #for j in range(num_of_iterations):
        #print(agents)       #checking shuffling
        #print(num_of_agents,len(agents))
    random.shuffle(agents)
        #print(agents)       #checking shuffling
    
    for i in range(no_of_wolves):
#        print("loop, total_sheep_eaten: ", total_sheep_eaten)    #used to check total_sheep_eaten updating correctly
        wolves[i].chase(num_of_agents, agents, total_sheep_eaten)
        matplotlib.pyplot.scatter(wolves[i]._x,wolves[i]._y, s=60,marker = "X")
#        print("before traverse",wolves[i]._x,wolves[i]._y )
        wolves[i].traverse()
#        print("after traverse",wolves[i]._x,wolves[i]._y )
#        print("hour count: ", hour_count) checks hour_count
        if hour_count%24 == 0: # to reset hour_counter every 24 iterations
            print("no of sheep wolf has eaten: ", wolves[i].sheep_eaten)
            print("wolf is hungry again")
            wolves[i].sheep_eaten = 0
            print("sheep eaten reset to: ",wolves[i].sheep_eaten)
#   for i in range(num_of_agents):    #removed to deal with removing agents
    for agent in agents:
        agent.move()
         #agents[i].move()
        #agents[i].eat()
        agent.eat()
        #print("store before sharing, agent: ",i, agents[i].store)
        #agents[i].share_with_neighbours(neighbourhood)
        agent.share_with_neighbours(neighbourhood)
#print("store after, agent:",i, agents[i].store)  #testing share with neighbour
# =============================================================================
# #testing section from practical 5
# a = practical6_agentframework.Agent(environment)
# print("a: ", a)
# print("a._y", a._y, "a._x: ", a._x) 
# a.move()
# print("a._y", a._y, "a._x: ", a._x)
# 
# =============================================================================
        

#stopping condition
# =============================================================================
# #   for i in range(num_of_agents):# removed to allow for removing agents
#     for agent in agents:    
#         
# =============================================================================
        #print("sheep full", sheep_full)
        #if agents[i].store >= full_belly:     #stops when all sheep have eaten at last 30
        if agent.store >= full_belly:    
            sheep_full += 1
           # print("sheep_full after checking store:", sheep_full)
        if sheep_full == len(agents):    
            carry_on = False
            print("stopping condition")
            print("Full belly: ", full_belly)
#plot the agents final position after eating and moving

    #for i in range(num_of_agents):         #removed to allow removing agents
    for agent in agents:    
        #matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
        matplotlib.pyplot.scatter(agent._x,agent._y)

def gen_function(b = [0]): # limits code to nopt running more than num of iterations
    """
    Defines stopping condition dependent on defined number of iterations and carry_on
    """
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations-1) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# =============================================================================
# adds a function that will run model. This is connected to the menu 
# such that when the menu is clicked, this function will run, in line with 
# the event based programming model
# 
# =============================================================================
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
def run():
    """
    Runs the animation displaying sheep and wolves for each iteration
    """
    print("running")
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,
                                        repeat=False, frames=gen_function)
    canvas.draw()#replaced canvas.show with canvas.draw
    #canvas.show()
    #needed instead of matplotlib.pyplot.show()
    #print("canvas drawn") #testing run order of model
    
    
"""
close the TKinter windows
"""
def finish():
    """
    Closes winows, notifies how many sheep killed and prints number of wolves
    """
    matplotlib.pyplot.close(fig)#moved to here
    print("no of wolves:", no_of_wolves)
    root.quit() # testing
    root.destroy()
#    matplotlib.pyplot.close(fig)
#    exit() # test
    messagebox.showwarning("Warning", str(total_sheep_eaten[0])+" sheep eaten")
    #os._exit(1) prevents files being written at end but prevents exception error
    # =============================================================================
# a second file: agents_stores.txt that writes out the total amount stored by 
# each of the agents on a line. Appends the data to the file, rather than
# clearing it each time it runs. This writes out the store value for each agent
# =============================================================================
    """
    append each agents store value to agents_stores.txt on one line
    """
    agents_stores = open("agents_stores.txt", 'a', newline="")
    agents_store_line = []
    for agent in agents:
        agents_store_line.append(agent.store)
    w = csv.writer(agents_stores, delimiter=',')
    w.writerow(agents_store_line)
    agents_stores.close()
    
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
    environment_eaten.close()    
    """
    append model data to model_data.txt
    """
    model_data = open("model_data.txt", 'a', newline="")
    model_data.write(str(datetime.now()))
    model_data.write("\nNo of sheep: ")
    model_data.write(str(num_of_agents))
    model_data.write("\nNo of iterations: "+ str(num_of_iterations))
    model_data.write("\nNo of wolves: " + str(no_of_wolves))
    model_data.write("\nNo of sheep eaten: " + str(total_sheep_eaten[0]))
    model_data.write("\nNo of alive sheep full: " + str(sheep_full))
    model_data.write("\nCarry on stopping condition (all sheep full) applied \nbefore number of iterations reached: "
     + str(not(carry_on)))
    model_data.write("\nEnd of model run \n \n \n")
    model_data.close()

#note gui needs to be exited using the drop down menu and selecting END
#for these files to be written




canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 



#just showing menu elements

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="END", command=finish)
tkinter.mainloop()  # replaced tkinter.mainloop() with root.mainloop()
# =============================================================================
# root.quit() # used in testing to get rid of sytemexit exception whne running pydoc
# root.destroy() # 
# sys.exit()
# =============================================================================
#Uses Tkinter - if running in Spyder set "Graphics" to Tkinter


#testing each agent has list of agents. 
#print(agents[0].agents[1].x) # printing x value of another agent





