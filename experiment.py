#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

experiment - Adaptation of Marrrtennjn's matlab experiment

flip & kayla & kriti @ skidmore

changelog:

10Jun13	flip 	created
'''

# psychopy things
from psychopy import visual, core, event, misc, gui

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

myWin = visual.Window([1000, 1000], monitor='testMonitor', units='pix')

myMouse = event.Mouse(win=myWin)

import csv
 
datafile = (CommentedFile(open('File.exp')))
reader = csv.reader(datafile)
header = reader.next()
data = [row for row in reader]

np.random.shuffle(data)
print data

tiltInfo = []
coordinates = [data]

i, j = data[0]
daG = GaugeFigure.GaugeFigure(myWin, myMouse, origin=[i, j], radius=50.0)

myDlg = gui.Dlg(title ="PyGauge")
myDlg.addField('Initials:')
myDlg.show()
if gui.OK:
    thisInfo = myDlg.data
else: print 'user cancelled'

while len(data) > 0:
    for key in event.getKeys():
        if key in ['escape', 'q']:
            print('done')
            core.quit()
        if key in ['space', 'enter']:
            tiltInfo.append((theta, phi, i, j))
            del data[0]
            try:
                i, j = data[0]
                daG = GaugeFigure.GaugeFigure(myWin, myMouse, origin=[i, j], radius=50.0)
                continue
            except:
                with open('pyGaugeOutput.csv', 'rb') as f:
                    bob=list(csv.reader(f))
                writer=csv.writer(open('pyGaugeOutput.csv','a'))
                writer.writerow(thisInfo)
                writer.writerow(('phi', 'theta', 'x', 'y'))
                for row in bob:
                    writer.writerow(tiltInfo)
                    core.quit()
    daG.draw()
    myWin.flip()
    if myMouse.getPressed()[0] is 1:
        (theta, phi) = daG.handleMouseDown()
        print theta, phi
    else:
        continue
