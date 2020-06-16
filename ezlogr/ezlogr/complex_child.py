#Step 1: Import ezlogr
import ezlogr
import time

#Step 2: Set some tags
tags = ["Very cool app!", "non-prod"]

#Step 3: Set the filename.
filename = __file__

#Step 4: Make your logger instance.
logger = ezlogr.Ezlogr(filename=filename, tags=tags)

#Step 5: Make some logs!
logger.info("I'm writing a log from complex_child")

import Complexparent
my_obj = Complexparent.my_object(1,2)
my_obj.my_method()

