#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

gaugefigure - Adaptation of Marrrtennjn's matlab gaugefigure into python

flip & kayla @ skidmore

changelog:

26dec12 flip  and we're off-
29 May 13 kayla fixed the AttributeError that kept it from running successfully
'''

# psychopy things
from psychopy import visual, core, event, misc

# things we need to use over and over here for utility
import numpy as np

#from numpy import sin, cos, tan, arctan2, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray, dot
from numpy.random import random, randint, normal, shuffle

import scipy as sci
import scipy.linalg

# utility functions


def rotationVecToMat(vec, theta):
    ''' create rotation matrix as per MATLAB's vrrotvec2mat.
        create a matrix that will rotate theta degrees about the axis defined by vec
    '''
    s = np.sin(theta)
    c = np.cos(theta)
    t = 1 - c

    # normalize the vector
    (x, y, z) = vec / np.linalg.norm(vec)

    return np.array([
        [t * x * x + c,     t * x * y - s * z,  t * x * z + s * y],
        [t * x * y + s * z, t * y * y + c,      t * y * z - s * x],
        [t * x * z - s * y, t * y * z + s * x,  t * z * z + c]])


class GaugeException(Exception):
    '''generic exception class that I ripped from somewhere else'''
    def __init__(self, description, code, enum_type=None):
        self.description = description
        self.code = code
        self.enum_type = enum_type

    def __str__(self):
        return(self.description + ': code ' + hex(self.code))


class GaugeFigure(object):
    '''GaugeFigure - class for dealing with the gauge figure'''

    def __init__(self, win, origin=[0, 0], radius=1.0, thickness=3, phigain=200, edges=32):
        '''Set up the gauge figure ellipse + normal'''
        
        # raw stuff
        self.myWin = win

        self.radius = radius
        self.thickness = thickness
        self.phigain = phigain
        self.edges = edges

        # for tracking
        self.origin = origin
        self.mouseOrigin = [0, 0]

        # for converting to useful numbers
        self.theta = 0   # tilt
        self.phi = 0     # slant
        self.rotmat = np.identity(3)

        # psychopy shape stim
        self.ellipse = visual.ShapeStim(win=self.myWin,
            lineColor='red',
            lineWidth=thickness,   #in pixels
            fillColor=None,
            #vertices=sqrVertices,
            closeShape=True,
            pos= [0, 0],
            ori=0,
            interpolate=True,
            opacity=1.0,
            autoLog=False)

        # make a set of vertices, circle of radius radius
        d = np.pi*2 / self.edges
        self.ev = np.asarray([
            (np.sin(e*d) * self.radius, np.cos(e*d) * self.radius, 0.0)
            for e in xrange(self.edges)
        ])

        # set the verticies to the x,y of the ev
        self.ellipse.setVertices(list(self.ev[:, [0, 1]]), log=False)

        # the 'tack'
        self.tv = np.asarray([[0, 0, 0], [0, 0, self.radius]])

        return

    def __del__(self):
        return

    def handleMouseDown(self):
        ''' track the mouse as the button is down and set slant/tilt'''
        self.mouseOrigin = myMouse.getPos()
        while myMouse.getPressed()[0] is 1:
            self.mouseToSlantTilt(myMouse.getPos())
            self.draw()
            self.myWin.flip()

        return (self.phi, self.theta)

    def mouseToSlantTilt(self, dmouse):
        '''calculate the slant and tilt from the mouse location'''
        dx, dy = dmouse - self.mouseOrigin
        # print(dx, dy)

        self.phi = np.sqrt(dx ** 2.0 + dy ** 2.0) / self.phigain
        if self.phi > np.pi / 2:     # slant is limited to pointing perpedendicular to the screen.
            self.phi = np.pi / 2

        self.theta = np.arctan2(dy / 2.0, dx / 2.0)

        self.rotmat = np.dot(rotationVecToMat(np.array([0, 0, 1]), np.pi / 4.0),
                          rotationVecToMat(np.array([0, 1, 0]), np.pi / 8.0))
        print(self.rotmat)
        return

    def draw(self):
        '''draw me'''
        newdl = np.dot(self.rotmat, self.ev)
        self.ellipse.setVertices(self.newdl[:, (0, 1)])

        self.ellipse.draw()
        return

    def get_state(self):
        return None


if __name__ == '__main__':
    '''Test Code - 
    note that, if you're running this via the command line and you're using EPD 
    you've gotta make sure you're in 32 bit EPD or the window won't get created.'''

    from psychopy import visual, event

    print("go!")

    myWin = visual.Window([600, 600], monitor='testMonitor', units='norm')

    myMouse = event.Mouse(win=myWin)

    daG = GaugeFigure(myWin)

    clock = core.Clock()
    while True:
        for key in event.getKeys():
            if key in ['escape', 'q']:
                core.quit()

        daG.draw()
        myWin.flip()

        if myMouse.getPressed()[0] is 1:
            print(daG.handleMouseDown())
        else:
            continue


    print('done')
# end
    