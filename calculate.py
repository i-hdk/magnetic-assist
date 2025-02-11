#caps lock is constant
#x axis is where the magnets are line up on, z is up down 

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
ITERATION_STEP = 0.1

#iterate across x,y,z
#x: -10 to 10, y: -4 to 4, z: 0 to 25

for x in range(X_LOWER_BOUND,X_UPPER_BOUND+1,ITERATION_STEP):
    print(x)