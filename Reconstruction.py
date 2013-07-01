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

#TWO PROBLEMS: 
# CSV reader reads as strings instead of floats
# separating the data into 2 lists doesn't work as intended

#get the CSV reader up and running to read the data
#datafile = open('pyGaugeOutput_okay.csv', 'rU')
reader = csv.reader(open('pyGaugeOutput_okay.csv', 'rU'))
#reader.QUOTE_NONNUMERIC
#header = reader.next()
data = [row for row in reader]


print data  
#
#make some lists to sort the data by stim
#image1 = []
#image2 = []
#
#CSV reader loop to sort the data
#for row in data:
#    if row[0] == './test/2.png':
#        image2.append(row[3:4])
#    elif row[0] == './test/1.png':
#        image1.append(row[3:4])
#    else:
#        raise Exception('Something went wrong!')
#        break
#        
#checking if it worked
#print image1
#print image2
#
#
#convert slant/tilt settings in a normal vector
#normalvectors=[]
#for i in image1:
#    normalvectors.append(np.cos(image1[1])*np.sin(image1[0]),np.sin(image1[1])*np.sin(image1[0]),np.cos(image1[0]))
#
#convert normal vectors in depth gradients
#gradients=[]
#for i in image1:
#    gradients.append((i,1)/(i,3),(i,2)/(i,3))
#
#print normalvectors
