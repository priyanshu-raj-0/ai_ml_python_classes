# Here is how we can import modules in python

# # Pattern 1 : Import the whole module
# import math
# # Now use: math.sqrt(16)

# math.sqrt(16)
# pivalue = math.pi
# math.prod([1,2,3,4])



# ------------------------------------------------------------------------------


# # Pattern 2 : Import specific item from a module 
# from math import sqrt, pi, prod

# ans1 = sqrt(16)
# ans2 = pi
# ans3 = prod([1,2,3,4,5])



# ------------------------------------------------------------------------------

# import random

# num = random.randint(1,10)
# choice = random.choice(["apple", "banana", "orange"])



# ------------------------------------------------------------------------------

import datetime

todaydate = datetime.datetime.now()
print(todaydate)



# ------------------------------------------------------------------------------

# import os
# curren_dir = os.getcwd()
# print(curren_dir)



# ------------------------------------------------------------------------------

import json
data = {"name":"priyanshu raj", "age": 19}
json_string = json.dumps(data)






