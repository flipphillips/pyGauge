#These are just the functions from GaugeFigure.py
# 6 - 13 -13
#Kriti Kayla Flip

# psychopy things
from psychopy import visual, core, event

# things we need to use over and over here for utility
import numpy as np



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

    def __init__(self, win, mouse, origin=[0, 0], radius=1.0, thickness=3, phigain=200, edges=32):
        '''Set up the gauge figure ellipse + normal'''   
        # raw stuff
        self.myWin = win
        self.myMouse = mouse

        self.radius = radius
        self.thickness = thickness
        self.phigain = phigain
        self.edges = edges

        # for tracking
        self.origin = origin
        self.mouseOrigin = (0, 0)
        self.myMouse = mouse

        # for converting to useful numbers
        self.theta = 0   # tilt
        self.phi = 0     # slant
        self.rotmat = np.identity(3)

        # make a set of vertices, circle of radius radius
        d = np.pi*2 / self.edges
        self.ev = np.asarray([
            (np.sin(e*d) * self.radius, np.cos(e*d) * self.radius, 0.0)
            for e in xrange(self.edges)
        ])

        # psychopy shape stim
        self.ellipse = visual.ShapeStim(
            win=self.myWin,
            lineColor='red',
            lineWidth=thickness,
            fillColor=None,
            #vertices=list(self.ev),
            closeShape=True,
            pos=self.origin,
            ori=0,
            interpolate=True,
            opacity=0.8,
            autoLog=False)

        # the 'tack'
        self.tv = np.asarray([(0, 0, 0), (0, 0, self.radius)])

        # psychopy shape stim
        self.tack = visual.ShapeStim(
            win=self.myWin,
            lineColor='red',
            lineWidth=thickness,
            fillColor=None,
            #vertices=list(self.tv),
            closeShape=False,
            pos=self.origin,
            ori=0,
            interpolate=True,
            opacity=0.8,
            autoLog=False)

        return

    def __del__(self):
        return

    def handleMouseDown(self):
        ''' track the mouse as the button is down and set slant/tilt'''
        self.mouseOrigin = self.myMouse.getPos()

        while self.myMouse.getPressed()[0] is 1:
            self.mouseToSlantTilt(self.myMouse.getPos())
            self.draw()
            self.myWin.flip()

        return (self.theta, self.phi)

    def mouseToSlantTilt(self, dmouse):
        '''calculate the slant and tilt from the mouse location'''
        dx, dy = dmouse - self.mouseOrigin

        self.phi = np.sqrt(dx ** 2.0 + dy ** 2.0)    # / self.phigain
        if self.phi > np.pi / 2.0:     # slant is limited to pointing perpedendicular to the screen.
            self.phi = np.pi / 2.0

        self.theta = np.arctan2(dy / 2.0, -dx / 2.0)

        self.rotmat = np.dot(rotationVecToMat(np.array([0, 1, 0]), self.phi),
                             rotationVecToMat(np.array([0, 0, 1]), self.theta))

        return

    def draw(self):
        '''draw me'''
        newev = np.dot(self.ev, self.rotmat)
        self.ellipse.setVertices(list(newev[:, (0, 1)]))
        newtv = np.dot(self.tv, self.rotmat)
        self.tack.setVertices(list(newtv[:, (0, 1)]))

        self.ellipse.draw()
        self.tack.draw()
        return

    def get_state(self):
        return None