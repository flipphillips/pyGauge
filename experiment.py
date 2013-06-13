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


# pseudo-code for this see experiment.md

#def import_text(filename, separator):
#    for line in csv.reader(filter(lambda row: row[0]!='#', open(filename), delimiter='\t', skipinitialspace=True)):
#        if line:
#            yield line

#for data in import_text('test.exp', '/'):
#    print (data)



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

#tsv_file = csv.reader(CommentedFile(open("File.exp", "rb")), delimiter=',')
                     
                     

myWin = visual.Window([600, 600], monitor='testMonitor', units='cm')

myMouse = event.Mouse(win=myWin)

import csv
 
datafile = (CommentedFile(open('File.exp')))
reader = csv.reader(datafile)
header = reader.next()
data = [row for row in reader]

np.random.shuffle(data)
print data

daG = GaugeFigureDefs.GaugeFigure(myWin, myMouse, origin=[2, 2])



def SetAsOrigin(x_cor, y_cor):
    daG = GaugeFigureDefs.GaugeFigure(myWin, myMouse, origin=[x_cor, y_cor])
    

for x in data:
    SetAsOrigin(range(*data[0]))
    daG.draw()
    win.flip()

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
    
#    if "png" in row: next(tsv_file)

