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
verticesIndex = pandas.read_csv('faces.txt', header=None, delim_whitespace=True)
vertices = pandas.read_csv('vertices.txt', header=None, delim_whitespace=True)

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

#convert normal vectors in depth gradients
gradients=[]
for row_index, row in dataFrame.iterrows():
    gradients.append(row['x']/row['theta'])
    gradients.append(row['y']/row['theta'])
#we probably want this to print to a CSV and each iteration should be a new row
#this is because later we want to be able to iterate through each row since they correspond to each triangle

#print gradients
verts = [[0.4,.3], [.6,.7],[.8,.45],[.1,.4]]
faces=[[1,2,3],[3,3,1],[2,2,2]]

for f in range(len(faces)):
    print [verts[faces[f][j]] for j in range(3)]
    fullList = [verts[faces[f][j]] for j in range (3)]
    x1,y1 = fullList[0]
    x2, y2 = fullList[1]
    x3, y3 = fullList[2]



#relative depth differences in a triangle: between the first vertex and the other two
relativedepths=[]
gx = []
gy = []

#for row_index, row in index.iterrows():
#    x1.append(columns[0], row['x'])
    #columns isnt a thing so we need to figure out the way to get this working

#print x1


#can try to use nrows command: it reads a certain number of rows each time. So potentially, set up a loop where each time it reads 3 rows 
#(3 vertices per triangle) and then begins from the next three rows?
#pandas usecols command

#also, if you put things into square brackets, panda understands that as one data type: see: 
#http://stackoverflow.com/questions/12269528/using-python-pandas-to-parse-csv-with-date-in-format-year-day-hour-min-sec

#we can select by column like this:
#see: http://stackoverflow.com/questions/8916302/selecting-across-multiple-columns-with-python-pandas

