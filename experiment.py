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

import os
from glob import glob 



#rules about hanshtags and such within the data file that provides coordinates for gauge figures
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



#get participant information
myDlg = gui.Dlg(title ="PyGauge")
myDlg.addField('Initials:')
myDlg.show()
if gui.OK:
    thisInfo = myDlg.data
else: 
    print 'user cancelled'
    core.quit()

# create output file
writer=csv.writer(open('pyGaugeOutput_'+thisInfo[0]+'.csv', 'w'))
writer.writerow(('stim', 'x', 'y', 'theta', 'phi'))

# get the input file
stimDir = "test"
stimList = glob("./"+stimDir+'/*.png')

for stim in stimList:
    
    myWin = visual.Window([1000, 1000], monitor='testMonitor', units='pix')
    myMouse = event.Mouse(win=myWin)

    datafile = (CommentedFile(open('File.exp')))
    reader = csv.reader(datafile)
    header = reader.next()
    data = [row for row in reader]
    
    np.random.shuffle(data)
    print data
    
    # our data
    tiltInfo = []
    
    # our things to draw with and stuff
    daG = GaugeFigure.GaugeFigure(myWin, myMouse, radius=25.0)
    stimPic=visual.ImageStim(win=myWin, image=stim)
    
    # probe loop
    for probePos in data:
        
        # randomize probe orientation
        daG.resetSlantTilt()
        
        done = False
        while not done:
            
            # set the position of the gague figure and draw everyone
            daG.setPos(probePos)
            stimPic.draw()
            daG.draw()
            myWin.flip()
            
            # first... the key logic
            for key in event.getKeys():
                # panic
                if key in ['escape', 'q']:
                    print('panic done')
                    core.quit()
                    
                # done with this point
                if key in ['space', 'enter']:
                    tiltInfo.append((stim, probePos[0], probePos[1], theta, phi))
                    done = True
                        
            # now, the mouse logic
            if myMouse.getPressed()[0] is 1:
                daG.startMouseDown()
                # monitor mouse and update
                while myMouse.getPressed()[0] is 1:
                    daG.whileMouseDown()
                    stimPic.draw() #draw image
                    daG.draw()#draw gauge figure
                    myWin.flip()
                    (theta, phi) = daG.stopMouseDown()
                print theta, phi
            

   
    # done withi this stim... write the stuff
    for aRow in tiltInfo:
        writer.writerow(aRow)

core.quit()
# and were done