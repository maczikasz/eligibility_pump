# ai-self-driving-car

# The following libraries are needed to run
* tensorflow or keras
* numpy
* matplotlib


Parameters to on main.py:
    *-im -- (im = implement) - Select implementation to run
    *-sb -- (sb = Start Brain) - Name of brain to start with, from saves/brains')
    *-eb -- (eb = End Brain) - Name of brain to write to after the iterations are done, from saves/brains')
    *-en -- (en = eligibility trace steps n) - How many steps should eligiblity trace steps take (1 is default, is simple one step Q learning)
    
Forexample, here tensorflow (the currently only ai running) where the end brain
that will be saved will be called brainski. Further more is the eligibility
trace set to 10

python main.py -im tf -eb brainski -en 10


TCP connect receiver and send port by running Simulink model <TestModel_3a.slx>. (notice first time starting Simulation can result in 
no connection to TCP/IP server established by python. Simply just run the script again and start the simulation yet again)