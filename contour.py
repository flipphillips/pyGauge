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

from numpy.random import random, randint, normal, shuffle

# test stuff
stimList = ["test/1.png", "test/2.png"]

myWin = visual.Window([1280, 1024], monitor='testMonitor', units='pix')
myMouse = event.Mouse(win=myWin)


for stim in stimList:
    im = visual.ImageStim(myWin, image=stim)
    im.draw()
    myWin.flip()

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
