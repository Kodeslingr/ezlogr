#!/usr/bin/env python3
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
logger.info("yeah")
time.sleep(1)
logger.info("no")
