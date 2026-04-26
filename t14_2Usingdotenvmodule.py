
# first we have to create .env file.


"""
What is a .env file?
A .env file is a simple text file that stores your environment variables. Instead of typing export commands, you write them once in a file.


Basic setup

1. Install python-dotenv

2. Create .env file

# .env
API_KEY=sk-1234567890abcdef
DATABASE_URL=sqlite:///myapp.db
DEBUG=True

3. Load in Python
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
That's it! Much easier than export commands.


"""

import os
from dotenv import load_dotenv

api_key = os.environ.get("API_KEY")
database_url = os.environ.get("DATABASE_URL")
debug = os.environ.get("DEBUG")

print(f"API KEY: {api_key}")
print(f"Debug mode: {debug}")
print(f"Database: {database_url}")

