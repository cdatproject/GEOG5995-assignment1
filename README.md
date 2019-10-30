# GEOG5995-assignment1

The final model sheep_wolf_model.py was developed in stages (1-9). Testing from earlier stages were removed from the final model
but left in the earlier versions. Please look at models 1-9 (Practicali_model.py) to see the testing. 
Where I have noted below ****EXTRA this indicates I have included some extra code not in the final 
model (sheep_wolf_model.py) so please look at these versions too. Below I list the features which were added in at 
each stage of the development.

The model is called "sheep_wolf_model.py" and uses the "sheep_wolf_framework.py". It also requires "in.txt" and an 
internet connection to work (to get data.html). Otherwise there is a copy of data.html in this repository in the 
"docs" folder. The docs folder also includes a folder with all the pydoc documentation for the sheep_wolf_model and the practicals.

Sheep_wolf_model has been set up to run from a shell.
It expects 3 parameters: num_of_agents , num_of_iterations , neighbourhood 
eg  python sheep_wolf_model.py 10 10 10
If there's less than 3 arguments (or wrong type of argument) it will produce an error message.
If there's more than 3 arguments it will exit.
To run from within an IDE such as Sypder comment out the sys.argv lines 50-65 and uncomment the lines setting these 3 variables

This is an agent based Python model running in a GUI containing two classes - Agents and Wolves.
The Agents represent sheep grazing an environment which is representing an outdoor landscape and the second 
agents, Wolfs, represent wolves. The x and y variable have been protected using the "_x" and "_y" and  
the property() function defines the property of both the Agent and Wolf classes but no value constraints have been
been applied to the getter, setter or deleter . 

Each agent is constructed with  _y,_x variables, "environment" list and list of "agents" passed into it.
Each agent has a store attribute which is initialised with value = 0

The Agent class has the following methods:
eat() - agent eats 10 if environment is >10 at (y,x) or remainder if environment <10
move() - agent's y and x move randomly +-1, torus solution added to deal with boundary effects (on 300x300 grid)
distance_between() - calculates distance between 2 agents
share_with_neighbour() - checks if any other agents are within defined distance (neighbourhood). If they are,
						it adds the two stores together and assigns the average to each store.

Each wolf is constructed with a list of agents(sheep), _x, _y passed into it. Each wolf has a sheep_eaten attribute 
which is initialised with value = 0. This increases by 1 for each sheep eaten, and is reset to 0 every 24 iterations.						

The Wolf class has the following methods:
traverse()	wolf traverse randomly + or - 3 in the x -axis direction
chase() - 	If wolf is closer than 10 units in x or y direction to an agent and the wolf has eaten less than 3 agents 
			in a 24 iteration period the wolf moves to the agent's (y,x) position and deletes (eats) the agent.
			sheep_eaten
			Prints number of sheep left and total sheep eaten
		 

The environment is read in from a 2 dimensional raster file (300x300) and the sheeps(y,x) coordinates are scraped 
from a web page in the [0,100] range (previous versions of the model in the submission folder show how these can 
be generated randomly instead). The co-ordinates scraped in from the webpage only cover a 100x100 grid, whereas 
the environment is 300x300.
no_of_wolves is randomly generated from a range dependent on the number of sheep. The wolf (y,x) coordinates are 
generated randomly with y in [0,100] and x in [0,300]

Running the model (sheep_wolf_model.py) opens 2 windows ("Figure 1" and "Sheep"). Both windows must be left open. 
In the "Sheep" window select "Run model" from the "Model" dropdown menu to run the model. The sheep are plotted 
with circles and the wolves are plotted by crosses. Select "END" from the "Model" dropdown menu when you are finished.

A message will pop up saying how many sheep have been eaten and the print output will tell you how many wolves 
there were. An output file called model_data.txt is appended to for each run and will list the time it ran, number 
of agents, number of iterations, number of wolves, and number of sheep eaten. 
Note: 
If running the model from Spyder ensure Tkinter is selected from the "Graphics backend" dropdown list in the 
graphics tab in Tools>Preferences>IPython console> 

Practical1_model.py  -		Makes 2 agents
							Moves 2 agents num_of_iterations iterations 
							calculates distance betwen 2 agents

 
Practical2_model.py - 		Creates agent list, with coordinates generated randomly for num_of_agents agents
							Uses indexed list referencing
							Plots 2 agent final positions using Matplotlib
							****EXTRA - plots most easterly point red
						
Practical3_model.py			Shrinks code to move num_of_agents agents
							Implements torus solution to deal with boundary effects
							Plots num_of_agents agents
						
Practical4_model.py 		Records times for model to run for different numbers of agents using perf_counter and magnitudes_of_agents
							Defines distance_between function, eliminating duplicate testing between agents
							****EXTRA plots num_of_agents against time taken for model to run
							****EXTRA prints minimum and maximum distance between agents

Practical5_model_xy.py		Creates agents using Agent class in agentframework.py
							num_of_agents created and added to agents container
							agents move num_of_iterations iterations
						

Practical5_Agentframework_xy	each agent has (y,x) between [0,100] randomly generated					
								move behviour added to Agent class - (y,x) move +/-1 randomly
								protects variable using _x and _y
								sets up property() attribute for x and y
				
Practical6_model_xy.py		uses csv reader to import in.txt raster file into environment
							****EXTRA sets x and y possible dimensions same as environment
							pass environment into each agent when it is created
							eat() called for each agent after move()
							****EXTRA environment written out to environment_eaten.txt at the end
							****EXTRA agents_stores.txt created with total amount stored by all the agents on a line, appended for each time model runs
							****EXTRA appends total of all agents stores to all_agents_stores_total.txt
							
Practical6_Agentframework_xy	pass environment variable into Agent constructor
								****EXTRA passes x_dimension and y_dimenson into constructor function
								Create store for each agent with starting value = 0
								define eat() for sheep to eat 10 if environment >=10 at its location
								__str__(self) overriden to display coordinates and store 
								else added to eat() so agents eat last bits without leaving negative values
								****EXTRA if added to eat() for agent(sheep) to be sick if store >100
								
practical7_model.py			all agents contain list of all other agents
							Added neighbourhood variable - defines distance within share_with_neighbour is called
							Shuffles agent order before each iteration to prevent model artifacts
							adds in sysargv arguments to run from command line setting num_of_iterations, num_of_agents and neighbourhood from command line call
							note practical7_model.html generated with sysargv commented out due to issue with pydoc running
							
practical7_Agentframework.py	Create distance_between() method to define distance between 2 agents
								Create share_with_neighbour method 
							- if distance between 2 agents < neighbourhood then both stores set to the average of both stores

practical8_model.py			Plots the agents after each iteration using update() function within FuncAnimation
							defines generator function gen_function() to use as frames argument
							gen_function() uses 2 stopping conditions - carry_on and num_of_iterations
							carry_on set to false when all sheep have eaten at least 300
							Removed code writing agent stores to agents_stores.txt, environment_eaten.txt and all_agents_stores_total.txt
							
practical8_Agentframework.py no updates


In creating the webpage I used lessons from https://www.w3schools.com and ideas from www.quackit.com 
to help with thr dropdown menus.
 
