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
# pseudo-code for this see experiment.md

def import_text(filename, separator):
    for line in csv.reader(filter(lambda row: row[0]!='#', open(filename), delimiter=separator, skipinitialspace=True)):
        if line:
            yield line

for data in import_text('test.exp', '/'):
    print (data)