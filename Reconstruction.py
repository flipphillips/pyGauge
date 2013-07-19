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
print gradients 
verts = [[0.4,.3], [.6,.7],[.8,.45],[.1,.4]]
faces=[[1,2,3],[3,3,1],[2,2,2],[1,3,3]]
#this is the data that we are using until we have a CSV format / file setup
count = 0
relativedepths = []
print len(faces)
for f in range(len(faces)): #loop for calculating depth gradients for triangle sides
    count = count+1 #used to keep moving through the gradients list later
    print [verts[faces[f][j]] for j in range(3)] #testing
    fullList = [verts[faces[f][j]] for j in range (3)]
    x1,y1 = fullList[0]
    x2, y2 = fullList[1]
    x3, y3 = fullList[2] #assigning variables
    print x1
    for g in range(len(gradients)):
        gx = gradients[count-1]
        gy = gradients[count]
        break
    relativedepths.append(gx*(x2-x1)+gy*(y2-y1))
    relativedepths.append(gx*(x3-x1)+gy*(y3-y1)) #calculating relative depths and appending to list
    for row in faces: #here we are trying to copy the matlab code with making a list "x" 
        bob = np.array([[row[0], row[1]],[row[0],row[2]]])
        print bob
        break
    #for i in range(len(relativedepths)-1):
    #this is the loop for creating a matrix with relative depths and faces -- called "m" in matlab code
    for i in range(len(bob)): #we can change this length to len(relativedepths) once all the files agree... when they have corresponding values
        a = np.zeros(len(bob)) #same here
        b = np.vstack((a, bob))
        c = np.ones(len(bob))
        d = np.vstack((b, c))
        e = np.linalg.inv(d) #in order to take the inverse, we need the data to correspond... otherwise the matrix isnt square and it doesn't work
        print e 

print relativedepths
