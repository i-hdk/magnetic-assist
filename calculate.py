#caps lock is constant
#x axis is where the magnets are line up on, z is up down 

import numpy as np

PENDULUM_MASS = 16.53 #g, includes magnet + hanging mass
STRING_LENGTH = 15 #cm
HOVER_HEIGHT = 3 #cm, height of magnet above ground when at rest & no magnets underneath
GRAVITY_ACCELERATION = 9.81 #m/s^2
DIPOLE_MOMENT = 1.2 #Am^2 guessed
MAGNET_SIZE = 0.9 #cm

#iteration constants (cm)
X_LOWER_BOUND = -10
X_UPPER_BOUND = 10
Y_LOWER_BOUND = -4
Y_UPPER_BOUND = 4
Z_LOWER_BOUND = 0
Z_UPPER_BOUND = 25
DEGREES_LOWER_BOUND = -90 #left (towards -x side) and 0 points to the bottom middle
DEGREES_UPPER_BOUND = 90
ITERATION_STEP = 1 #final should be around .1, big num for debug/testing only
            
for deg in np.linspace(DEGREES_LOWER_BOUND,DEGREES_UPPER_BOUND, num = int((DEGREES_UPPER_BOUND-DEGREES_LOWER_BOUND)/ITERATION_STEP)+1):
    print(deg)    

