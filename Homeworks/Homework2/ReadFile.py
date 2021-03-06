# this file contains a function which will read in a file and output the time in Myr, the total number of particles, and all of
# the particle data (type, mass, x, y, z, vx, vy, vz) as an array 

import numpy as np # importing numpy module
import astropy.units as u # importing astropy.units module

def Read(filename): # define Read function
    file = open(filename,'r') # opens file, 'r' indicates 'reading' mode
    line1 = file.readline() # reads first line of file, assigns name of 'line1'
    label, value = line1.split() # splits line1 string into list based on delimiter of tab, calls first thing in list
    # 'label' and second thing 'value'
    time = float(value)*u.Myr # uses astropy to assign time units of Myr
    
    line2 = file.readline() # reads second line of file, assings name of 'line2'
    label2, number = line2.split() # splits line2 into list, calls first thing 'label2' and second 'number'
    
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3) # stores rest of data in an array. 'None'
    # splits line via white spaces, '3' skips first 3 lines of file, 'True' stores data with labels specified in file
    file.close() # closes file
    return time, number, data # outputs time, total number of particles, and data array

