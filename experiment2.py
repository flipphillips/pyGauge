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
from numpy import genfromtxt
import csv
import sys, re
import pandas as pd

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

tsv = pd.read_csv("File.exp", delimiter=',', names=['co_x','co_y'], header = None, comment = '#')


list1 = df.co_x.to_list()
list2 = df.co_y.to_list()

#VSS = []
#
#for row in tsv_file:
#    if row != int:
#        next(tsv_file)
#    if row:
#        print row
        

#for row in tsv_file:
#    if row:
#        print row
    
    
#    if "png" in row: next(tsv_file)

