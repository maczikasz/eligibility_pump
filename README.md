# ai-self-driving-car

# The following libraries are needed to run
* kivy
* pytorch or tensorflow
* numpy


Parameters to on map.py:
    --simulation -- run the app without a UI
    --ui  -- run the app with UI showing the car insect
    --start_brain -- filename (it must be stored in "./saves/brains/$filename" to start brain, which will be loaded before any action happens (for TF need to have .meta extension),
    --end_brain -- only for simulation, the name of the brain to save the model to (it will be saved to "./saves/brains/$filename"
    --iterations -- only for simulation, the number of updates to be run