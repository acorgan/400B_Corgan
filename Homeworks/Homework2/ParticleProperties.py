# this file contains a function which will read in a file with a particle type and number specified, and then return the mass, distance, and velocity of that particle

from ReadFile import Read # imports read function from previous part of homework
from math import sqrt # imports need square root function for magnitude calculations
import numpy as np # imports numpy module
import astropy.units as u # imports astropy.units module

def ParticleInfo(filename,ptype,pnum): # defining function 
    time,number,data = Read(filename) # assigns variables to output of Read function, will only use 'data' in this function
    index = np.where(data['type'] == ptype) # creates index array based on particle type specified so that first and last entries correspond to the position of the first
    # and last particles of that type in the file
    m = data['m'][index[0][pnum-1]]*(10**10)*u.solMass # gets mass of specified particle. '[0]' is needed to specify row of index matrix '[pnum-1]' shifts the index so that
    # the number inputted actually corresponds to that number particle in the list. gives mass units of 10^10 solar masses
    x = data['x'][index[0][pnum-1]] # getting position and velocity components for particle in the same way mass was retrieved. 
    y = data['y'][index[0][pnum-1]]
    z = data['z'][index[0][pnum-1]]
    vx = data['vx'][index[0][pnum-1]]
    vy = data['vy'][index[0][pnum-1]]
    vz = data['vz'][index[0][pnum-1]]
    r = sqrt(x**2+y**2+z**2)*u.kpc # gets magnitude of position, assigns units of kpc
    v = sqrt(vx**2+vy**2+vz**2)*u.km/u.s # gets magnitude of velocity, assigns units of km/s
    rround = np.around(r,3) # rounds position magnitude to 3 decimal places
    vround = np.around(v,3) # rounds velocity magnitude to 3 decimal places 
    msci = "{:e}".format(m) # makes it so mass is displayed in scientific notation
    return rround,vround,msci # gives rounded position magnitude, rounded velocity magnitude, and particle mass as outputs
