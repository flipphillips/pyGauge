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
import GaugeFigure

import csv
import sys, re

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
    daG = GaugeFigure.GaugeFigure(myWin, myMouse, origin=[i, j], radius=50.0)
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