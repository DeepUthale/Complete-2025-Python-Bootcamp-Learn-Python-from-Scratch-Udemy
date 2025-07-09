# Two types of modules in python:
#   - Built in Modules
#   - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
import math
import os
import my_module
import requests

print(math.sqrt(16)) # Built in Module

my_module.hello() # User defined module

req = requests.get("https://www.google.com") # External Module
print(req.text)
