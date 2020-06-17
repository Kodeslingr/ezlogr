# EZlogR for Python!
## Overview
This module helps developers focus on writing code and less time worrying about writing logs. 

## How it works
EZlogR gives a standardized way for developers to write logs, and creates these logs in JSON format. JSON is easily digestable by a multitude of programs and databases. This lets the developer have the option to easily pull the logs into something like MongoDB, a JSON viewing tool, or still be easily human readable due to the simplified and flat nature of the JSON packing.

## Installation
install EZlogR using pip or pip3: <br>
`pip install ezlogr`<br> 
or<br>
`pip3 install ezlogr`

## Usage
Below is a simple python file that shows EZlogR in action:

```
#!/usr/bin/env python3
#Step 1: Import ezlogr
import ezlogr

#Step 2: Set some tags
tags = ["Very cool app", "non-prod"]

#Step 3: Set the filename for your logs. (This will automatically append .log to the .py filename like this: 'myfile.py.log')
filename = __file__

#Step 4: Make your logger instance.
logger = ezlogr.Ezlogr(filename=filename, tags=tags)

#Step 5: Now write your code with EZlogR!
import time
logger.info("Here I go writin' logs!")
time.sleep(1)
logger.info("I'm doing it again!")
```

