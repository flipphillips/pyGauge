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

    lines = visual.ShapeStim(
        myWin,
        lineColor='red',
        lineWidth=3.0,  # in pixels
        fillColor=None,  # beware, with convex shapes fill colors don't work
        closeShape=True,  # do you want the final vertex to complete a loop with 1st?
        pos= [0,0],  # the anchor (rotaion and vertices are position with respect to this)
        interpolate=True,
        opacity=0.5,
        autoLog=False)

    # event loop
    while True:
        if myMouse.getPressed()[0] is 1:
            outPts.append(myMouse.getPos())
            event.clearEvents()
            lines.setVertices(list(outPts))

        for key in event.getKeys():
            print key
            if key in ['escape', 'q']:
                print(str(outPts))
                core.quit()
            elif key in ['space', 'enter']:
                print(str(outPts))
                return outPts
            elif key in ['backspace']:
                print(outPts.pop())
                lines.setVertices(list(outPts))

        im.draw()
        lines.draw()
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
