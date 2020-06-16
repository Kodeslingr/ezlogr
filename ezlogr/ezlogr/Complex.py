#!/usr/bin/env python3

#Step 1: Import ezlogr
from ezlogr.ezlogr.ezlogr import Ezlogr
import time

#Step 2: Set some tags
tags = ["Very cool app!", "non-prod"]

#Step 3: Set the filename.
filename = __file__

#Step 4: Make your logger instance.
logger = Ezlogr(filename=filename, tags=tags)


class Myobject(object):
    def __init__(self, a, b):
        logger.info("Just doing my setup method!")
        self.a = a
        self.b = b

    
    def my_method(self):
        logger.info("Running the my_function method!")
        print(self.a)
        print(self.b)
        print()
