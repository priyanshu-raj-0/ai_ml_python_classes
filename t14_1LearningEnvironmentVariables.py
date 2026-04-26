
# In this we are going to learn how to create a environment variable and how to use it 

"""

What are environment variables?
:- Environment variables are settings stored outside your code. Think of them as configuration that your program can read.


# Never hardcode sensitive data!
api_key = "sk-1234567890abcdef"  # Everyone can see this!
database = "production_database"  # Can't change without editing code

Problems:
Secrets visible in code
Can't share code safely
Different settings for different computers


How environment variables work :- Environment variables live in your system, not your code:


"""

import os

# Read from environment
api_key = os.environ.get('API_KEY')     # There is not default value of api_key
database = os.environ.get('DATABASE_NAME', 'default.db')  # default.db is a default value 

print(f"Using API Key: {api_key}")
print(f"Using database: {database}")


"""
Setting environment variables : You can set them temporarily in your terminal:

# Windows
set API_KEY=sk-1234567890abcdef
set DATABASE_NAME=database23-dxi234zxc
python app.py

But they disappear when you close the terminal!

"""


# we can get api_key from environment variable using these methods

# Method 1: Get with default
api_key = os.environ.get('API_KEY', 'demo-key')     # os.environ is a python dictionary type, and get is the method of the dictionary that gives the value of the related key, if key is not in the dictionary then it gives none, it don't produce error.


# Method 2: Check if exists
if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
else:
    print("No API key found")


# Method 3: Will crash if not found
api_key = os.environ['API_KEY']  # KeyError if missing! os.environ is a python dictionary type, and produce error when we are trying to accesses key that is not present in the dictionary



# Here is the example for the dictionary function for better understanding

dic = {
    "name" : "priyanshu raj",
    "class": "BCA-3",
    "college": "AN College",
    "University": "Patliputra University",
}

print(dic["name"])
print(dic.get("class"))
print(dic.get("age"))    # if key is not present in the dictionary then it gives none until it has not default value
print(dic.get("marks", "90.8%"))




"""

INSTEAD OF DOING ALL THIS WE CAN create a .env file 
that we learn in t14_2Usingdotenvmodule.py

what is module : module is a python file 
"""

