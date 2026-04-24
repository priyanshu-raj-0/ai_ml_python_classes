# This is a string 
string = "This is a string."
long_string = """
Hello,
This is Priyanshu raj, who is your's mentor for today.
How are you.
"""
print(long_string)

first_name = "Priyanshu"
last_name = "raj"
full_name = first_name + " " + last_name
long_dash = "-" * 50
print(full_name)
print(long_dash)
print(len(long_dash))
print(len(long_string))


# Here are some important method that is used in python
name = "Veer raj"
string = f"Hi there, my name is {name}"
print(string)
print(string.lower())
print(string.upper())
print(string.title())


string2 = "I love Python programming with Python"

print("Python" in string2)
print(string2.startswith("I"))
print(string2.endswith("python"))
print(string2.find("Python"))
print(string2.count("Python"))
print(len(string2))

string3 = string2.replace("Python", "javascript")
print(string3)