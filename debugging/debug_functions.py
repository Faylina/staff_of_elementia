#---------------------------------------#
#---------- DEBUG FUNCTIONS ------------#
#---------------------------------------#

#---------- IMPORTS -----------#
import inspect
from debugging.config import DEBUG

#---------- DEBUG FUNCTIONS ------------#

def debugMethod(self):
    if DEBUG:
        print(f"DEBUG: Calling the method {inspect.stack()[1].function} of the class {type(self).__name__} ")

def debugClass(self):
    if DEBUG:
        print(f"DEBUG: {type(self).__name__} object is being created.")