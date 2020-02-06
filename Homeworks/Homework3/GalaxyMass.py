# This program contains a function that will calculate the total mass of of all the
# particles of a given type in the galaxy specified.

from ReadFile import Read # Import read function to read the file
import numpy as np
import astropy.units as u

def ComponentMass(filename,parttype):
    # Inputs:
    #    filename is the name of the galaxy from which the data will be read
    #    parttype is the particle type to get the masses of
    #    halo is type 1, disk is type 2, bulge is type 3
    # Returns:
    #    total mass of particles of given type in 10^12 solar masses

    # Need to read file and assign outputs of Read function
    # time is time in 10 Myr, number is total number of particles, data is data array
    # data array has particle masses, which will be of interest here
    time,number,data = Read(filename)

    # set up an index which specifies all of the particles of the given type in data array
    index = (np.where(data['type']==parttype))

    # define 'mass' as an array which will be extended in a for loop with all particle masses
    # by iterating the loop over every value in 'index' 
    mass = []
    for i in index:
        mass.extend(data['m'][i])

    # 'mass' should now be a list of all particle masses of a given type. Now will sum all
    # of these masses and return the total mass, dividing by 100 gets mass in units of
    # x 10^12 solar masses, as the masses in the data array are in units of 10^10 solar
    # masses. np.around rounds the answer to 3 decimal places

    return np.around(sum(mass)/100.,3)*u.solMass

    

    
