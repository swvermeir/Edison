#-------------Setup----------------
import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------
speed = Ed.SPEED_1

none = 9999
path = none
grass = none
swamp = none

buffer = 50

Ed.LineTrackerLed(Ed.ON)

path = Ed.ReadLineTracker()

on_path = True
spin = Ed.SPIN_RIGHT
while True:
    color = Ed.ReadLineTracker()
    if on_path:
        if abs(color - path) < buffer:
    	    Ed.Drive(Ed.FORWARD_RIGHT, speed, Ed.DISTANCE_UNLIMITED)
    	    
    	elif grass == none:
    	    grass = color
    	    
    	elif abs(color - grass) < buffer:
    	    Ed.Drive(Ed.FORWARD_LEFT, speed, Ed.DISTANCE_UNLIMITED)
    	    
    	elif swamp == none:
    	    swamp = color
    	    
    	elif abs(color - swamp) < buffer:
    	    Ed.Drive(Ed.FORWARD, speed, 3)
    	    Ed.Drive(spin, speed, 90)
    	    path = False
    	    
    	else:
    	    Ed.Drive(Ed.FORWARD_LEFT, speed, Ed.DISTANCE_UNLIMITED)
		    
    else:
        if abs(color - swamp) < buffer:
            Ed.Drive(Ed.FORWARD, speed, Ed.DISTANCE_UNLIMITED)
            
        else:
            Ed.Drive(spin, speed, 90)
            Ed.Drive(Ed.FORWARD, speed, 5)
            Ed.Drive(spin, speed, 90)
            
            if spin == Ed.SPIN_RIGHT:
                spin = Ed.SPIN_LEFT
            else:
                spin = Ed.SPIN_RIGHT
