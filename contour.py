#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

contour - Adaptation of Marrrtennjn's matlab experiment

flip & kayla & kriti @ skidmore

changelog:

10Jun13	flip 	created
'''

# psychopy things
from psychopy import visual, core, event, misc

# things we need to use over and over here for utility
import numpy as np

#from numpy.random import random, randint, normal, shuffle

# for filenames
import os
from glob import glob

# we need to at least specify this.
stimDir = "test"
stimList = glob("./"+stimDir+'/*.png')

# ui elements
myWin = visual.Window([1280, 1024], monitor='testMonitor', units='pix')
myMouse = event.Mouse(win=myWin)


def doOne(fname):
    '''handle a stimulus'''

    outPts = []
    holePts = []
    ridgePts = []

    im = visual.SimpleImageStim(myWin, image=fname)

    # event loop
    while True:
        for key in event.getKeys():
            if key in ['escape', 'q']:
                print('done')
                core.quit()
            elif key in 

    im.draw()
    myWin.flip()

for stim in stimList:
    doOne(stim)

    while True:
        for key in event.getKeys():
            if key in ['escape', 'q']:
                print('done')
                core.quit()

        if myMouse.getPressed()[0] is 1:
            core.wait(1)
            break
        else:
            continue
