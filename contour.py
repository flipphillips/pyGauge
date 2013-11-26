#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

contour - Adaptation of Marrrtennjn's matlab experiment

flip & kayla & kriti @ skidmore

changelog:

10Jun13	flip 	created
'''

# psychopy things
from psychopy import visual, core, event

# things we need to use over and over here for utility
import numpy as np

#from numpy.random import random, randint, normal, shuffle

# for filenames
import os
from glob import glob
import csv

# we need to at least specify this.
stimDir = "test"
stimList = glob("./"+stimDir+'/*.png')

# ui elements
myWin = visual.Window([1280, 1024], monitor='testMonitor', units='pix')
myMouse = event.Mouse(win=myWin)
myText = visual.TextStim(myWin, text=u"here")


class GaugeContour(object):
    '''GaugeContour - contour class for dealing with the gauge figure'''

    def __init__(self, win, mouse, imageFileName, thickness=3,
                 lineColor='green', dotColor='blue'):
        '''Set up the gauge figure ellipse + normal'''

        # raw stuff
        self.win = win
        self.mouse = mouse
        self.thickness = thickness
        self.lineColor = lineColor
        self.dotColor = dotColor
        self.drawDots = True

        # image
        self.image = visual.SimpleImageStim(self.win, image=imageFileName)

        # line stim
        self.lines = visual.ShapeStim(self.win,
                                      lineColor=self.lineColor,
                                      lineWidth=self.thickness,
                                      fillColor=None, closeShape=False,
                                      opacity=0.75, autoLog=True)
        #
        self.points = []


def doOne(fname, outfname):
    '''handle a stimulus'''

    fileName, fileExtension = os.path.splitext(fname)

    outPts = []

    im = visual.SimpleImageStim(myWin, image=fname)

    lines = visual.ShapeStim(
        myWin,
        lineColor='red',
        lineWidth=3.0,  # in pixels
        fillColor=None,
        closeShape=False,
        pos=[0, 0],
        interpolate=True,
        opacity=0.5,
        autoLog=False)

    # event loop
    oldpos = (0, 0)
    while True:
        if myMouse.getPressed()[0] is 1:
            newpos = myMouse.getPos()
            if not np.array_equal(newpos, oldpos):
                outPts.append(newpos)
                event.clearEvents()
                lines.setVertices(list(outPts))
                oldpos = newpos

        for key in event.getKeys():
            print key
            if key in ['escape', 'q']:
                print(str(outPts))
                core.quit()

            elif key in ['space', 'return']:
                print(str(outPts))
                ofile = open(fileName+outfname, 'wb')
                writer = csv.writer(ofile, dialect='excel')
                for row in outPts:
                    writer.writerow(row)
                ofile.close()

                return outPts

            elif key in ['backspace']:
                print(outPts.pop())
                lines.setVertices(list(outPts))

        im.draw()
        lines.draw()
        myWin.flip()


for stim in stimList:
    myText.setText("Draw Boundary.\n Enter when done.\n Any key to continue.")
    myText.draw()
    myWin.flip()

    event.waitKeys()

    doOne(stim, "_border.csv")

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
