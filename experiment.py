#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

experiment - Adaptation of Marrrtennjn's matlab experiment

flip & kayla & kriti @ skidmore

changelog:

10Jun13	flip 	created
'''

# psychopy things
from psychopy import visual, core, event, misc

# things we need to use over and over here for utility
import numpy as np

from numpy.random import random, randint, normal, shuffle
import csv
import sys, re
import GaugeFigureDefs



import csv
import sys, re

# pseudo-code for this see experiment.md

#def import_text(filename, separator):
#    for line in csv.reader(filter(lambda row: row[0]!='#', open(filename), delimiter='\t', skipinitialspace=True)):
#        if line:
#            yield line

#for data in import_text('test.exp', '/'):
#    print (data)

<<<<<<< HEAD
=======


>>>>>>> Trial-Handler
class CommentedFile:
    def __init__(self, f, commentstring="#"):
        self.f = f
        self.commentstring = commentstring
    def next(self):
        line = self.f.next()
        while line.startswith(self.commentstring):
            line = self.f.next()
        return line
    def __iter__(self):
        return self

<<<<<<< HEAD
tsv_file = csv.reader(CommentedFile(open("test.exp", "rb")),
                      delimiter=' ')
                     

for row in tsv_file:
    if row != int:
        next(tsv_file)
    if row:
        print row
        


#for row in tsv_file:
#    if row:
#        print row
    
=======
#tsv_file = csv.reader(CommentedFile(open("File.exp", "rb")), delimiter=',')
                     
                     

myWin = visual.Window([600, 600], monitor='testMonitor', units='pix')

myMouse = event.Mouse(win=myWin)

import csv
 
datafile = (CommentedFile(open('File.exp')))
reader = csv.reader(datafile)
header = reader.next()
data = [row for row in reader]

np.random.shuffle(data)
print data

while len(data) > 0:
    i, j = data[0]
    daG = GaugeFigureDefs.GaugeFigure(myWin, myMouse, origin=[i, j])
    for key in event.getKeys():
        if key in ['escape', 'q']:
            print('done')
            core.quit()
    daG.draw()
    myWin.flip()
    if myMouse.getPressed()[0] is 1:
        (theta, phi) = daG.handleMouseDown()
        print theta, phi
        if myMouse.getPressed()[0] is 0:
            del data[0]
            print data
    else:
        continue

#for x in data:
#    SetAsOrigin(data[0],data[1])
#    daG.draw()
#    win.flip()

#
#for row in reader:
#    if row:
#        header = reader.next()
#        data.append()
#
#print data



#
#for row in tsv_file:
#    if row:
#        print row
#        
>>>>>>> Trial-Handler
    
#    if "png" in row: next(tsv_file)

