#Created by Kriti and Kayla
#7/1/13
#Reconstruction for PyGauge

# psychopy things
from psychopy import visual, core, event, misc, gui

# things we need to use over and over here for utility
import numpy as np

from numpy.random import random, randint, normal, shuffle
import csv
import sys, re
import GaugeFigure

import os
from glob import glob 

#get the CSV reader up and running to read the data
datafile = open('pyGaugeOutput_okay.csv', 'rU')
reader = csv.reader(datafile)
header = reader.next()
data = [row for row in reader]

#make some lists to sort the data by stim
image1 = []
image2 = []

#CSV reader loop to sort the data
for row in data:
    if row[0] == './test/2.png':
        image2.append(row)
    elif row[0] == './test/1.png':
        image1.append(row)
    else:
        raise Exception('Something went wrong!')
        break
        
#checking if it worked
print image1
print image2
core.quit()
