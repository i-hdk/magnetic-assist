#caps lock is constant
#x axis is where the magnets are line up on, z is up down 
import math
import numpy as np
import matplotlib.pyplot as plt

PENDULUM_MASS = 0.001653 #kg, includes magnet + hanging mass
STRING_LENGTH = 0.15 #m
HOVER_HEIGHT = 0.03 #m, height of magnet above ground when at rest & no magnets underneath
GRAVITY_ACCELERATION = 9.81 #m/s^2
DIPOLE_MOMENT = 1.2 #Am^2 guessed
MAGNET_SIZE = 0.9 #cm
MU_NAUGHT = 4*math.pi*1e-7 
MAGNET_DISTANCE_FROM_ORIGIN = 0.025 #m

#iteration constants (cm)
X_LOWER_BOUND = -10
X_UPPER_BOUND = 10
Y_LOWER_BOUND = -4
Y_UPPER_BOUND = 4
Z_LOWER_BOUND = 0
Z_UPPER_BOUND = 25
DEGREES_LOWER_BOUND = -90 #left (towards -x side) and 0 points to the bottom middle
DEGREES_UPPER_BOUND = 90
ITERATION_STEP = 1 #final should be around .1, big num for debug only

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def degreeToCoordinate (deg)->tuple:
    x = math.sin(math.radians(deg))*STRING_LENGTH
    z = HOVER_HEIGHT+STRING_LENGTH-math.cos(math.radians(deg))*STRING_LENGTH
    y = 0 #assuming one directional pendulum
    return (x,y,z)

def calculateDipole(x,y,z,d=DIPOLE_MOMENT)->np.ndarray:
    pendulum_string = np.array([0-x,0-y,HOVER_HEIGHT+STRING_LENGTH-z]) #direction from magnet to pivot
    unit = pendulum_string/np.linalg.norm(pendulum_string)
    return unit*d

#relative to base magnet or field producing dipole
def calculateR(bx,by,bz,x,y,z)->tuple:
    return (x-bx,y-by,z-bz)

def calculateMagneticField(mx,my,mz,r)->np.ndarray:
    m = np.array([mx,my,mz])
    r = np.array([r[0],r[1],r[2]])
    return MU_NAUGHT/(4*math.pi)*(3*np.dot(m,normalize(r))*normalize(r)-m)/(np.linalg.norm(r)**3)

def calculateMagneticPotentialEnergy (x,y,z)->float:
    b_left = calculateMagneticField(0,0,DIPOLE_MOMENT,calculateR(-MAGNET_DISTANCE_FROM_ORIGIN,0,0,x,y,z))
    #print("left magnet field",b_left)
    b_right = calculateMagneticField(0,0,DIPOLE_MOMENT,calculateR(MAGNET_DISTANCE_FROM_ORIGIN,0,0,x,y,z))
    #print("right magnet field",b_right)
    #print("r", calculateR(MAGNET_DISTANCE_FROM_ORIGIN,0,0,x,y,z))
    dipole = calculateDipole(x,y,z)
    return np.dot(-dipole,b_left) + np.dot(-dipole,b_right) #is this even in joules


min_energy = 0
first_iteration = True
best_location = (0,0,0)
best_gravitational_potential_energy = 0
best_magnetic_potential_energy = 0

#plot out pendulum points
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
x_points = np.empty_like(np.linspace(DEGREES_LOWER_BOUND,DEGREES_UPPER_BOUND, num = int((DEGREES_UPPER_BOUND-DEGREES_LOWER_BOUND)/ITERATION_STEP)+1))
y_points = np.empty_like(x_points) #actually z in calculations, y for simplicity (2d plotting)
energy_points = np.empty_like(x_points)
it = 0

#iterate deg bc assuming one directional pendulum        
for deg in np.linspace(DEGREES_LOWER_BOUND,DEGREES_UPPER_BOUND, num = int((DEGREES_UPPER_BOUND-DEGREES_LOWER_BOUND)/ITERATION_STEP)+1):
    print(deg)    
    print(degreeToCoordinate(deg))
    
    (magnet_x,magnet_y,magnet_z) = degreeToCoordinate(deg)       
    gravitational_potential_energy = PENDULUM_MASS*GRAVITY_ACCELERATION*(magnet_z-HOVER_HEIGHT)
    kinetic_energy = 0
    magnetic_potential_energy = calculateMagneticPotentialEnergy(magnet_x,magnet_y,magnet_z)
    energy = gravitational_potential_energy+kinetic_energy+magnetic_potential_energy
    print("gravity PE ",gravitational_potential_energy)
    print("magnetic PE ",magnetic_potential_energy)
    
    x_points[it] = magnet_x
    y_points[it] = magnet_z
    energy_points[it] = energy*2000 
    it+=1
    
    if first_iteration:
        min_energy = energy
        best_location = (magnet_x,magnet_y,magnet_z)
        first_iteration = False
        best_gravitational_potential_energy = gravitational_potential_energy
        best_magnetic_potential_energy = magnetic_potential_energy
    if energy<min_energy:
        min_energy = energy
        best_location = (magnet_x,magnet_y,magnet_z)
        best_gravitational_potential_energy = gravitational_potential_energy
        best_magnetic_potential_energy = magnetic_potential_energy
    
#plot
ax.scatter(x_points, y_points, s=energy_points, c=energy_points, edgecolors=(0,0,0),linewidths=0.5)
ax.set(xlim=(-0.15, 0.15),ylim=(0, 0.15))
plt.show()

print("lowest energy location:")
print(best_location)
print("best: gravity PE ",best_gravitational_potential_energy)
print("best: magnetic PE ",best_magnetic_potential_energy)


#debug
#print(calculateMagneticPotentialEnergy(0.023465169756034628, 0, 0.03184674891072933))
#print(calculateMagneticPotentialEnergy(0.025, 0, 0.03184674891072933))



    

