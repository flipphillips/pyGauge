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

import pandas
dataFrame = pandas.read_csv('pyGaugeOutput_okay.csv')
triangleVertices = pandas.read_csv('faces.txt')
print dataFrame

print dataFrame.describe()

#print dataFrame['x']

#print dataFrame[0:2]

#for row_index, row in dataFrame.iterrows():
    #print (row['x'] + row['y']) / 2.0


#convert slant/tilt settings in a normal vector
normalvectors=[]
for row_index, row in dataFrame.iterrows():
    normalvectors.append(np.cos(row['phi'])*np.sin(row['theta']))
    normalvectors.append(np.sin(row['phi'])*np.sin(row['theta']))
    normalvectors.append(np.cos(row['theta']))
print normalvectors


#convert normal vectors in depth gradients
gradients=[]
for row_index, row in dataFrame.iterrows():
    gradients.append(row['x']/row['theta'])
    gradients.append(row['y']/row['theta'])

print gradients

#relative depth differences in a triangle: between the first vertex and the other two
relativedepths=[]
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
gx = []
gy = []
relativedepths = []

for row_index, row in triangleVertices.iterrows():
    x1.append(