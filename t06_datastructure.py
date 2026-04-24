# List = [] , it can we changed (mutable)

has_licence = False

lst = ["priyanshu", 19, 90.8, has_licence, True]

# accessing the element of the list

name = lst[0]
age = lst[1]
marks_percentile = lst[2]
has_licence = lst[-2] # using negative index
boolean = lst[-1]

for i in lst:
    print(i)

fruits = ["apple", "banana", "orange", "coconut", "grapes", "guava", "mango"]


first = fruits[0]
last = fruits[-1]
print(fruits)
# slicing the list
sliced_fruits = fruits[2:]
print(sliced_fruits)

sliced_fruits = fruits[2:6]
print(sliced_fruits)

# updating the elements of the list

fruits[0] = "lichi"
print(fruits)

fruits.append("apple")
print(fruits)

fruits.index("coconut")
fruits.insert(3,"pineapple")

print(fruits)

fruits.extend("plum")
print(fruits)

# to see more methods simply type : fruits.

numbers = [1,4,7,8,5,6,1,3,12,3,2,44,1,3]
numbers.count(1)
len(numbers)
numbers.index(44)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)



# Dictionaries = {} , it can we changed (mutable)

student = {
    "name" : "priyanshu raj",
    "age" : 19,
    "marks" : 90.5,
    "city" : "Bakhtiyarpur",
}
print(student)

student["name"]
student["age"]
student["marks"]
student["city"]

student["has_licence"] = True
print(student)

del student["has_licence"]
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

for i in student.items():
    print(i)

for i in student.items():
    print(i[1])

if "name" in student:
    print("name found!!")


# Tuples = (), it can't be changed (immutable)

co_ordinate = (2,3)
rgb = (212, 122, 12)
color = ("red", "green", "blue")
point = (3,5)

color[-1]
# color[0] = "black" #Doesn't support item assignment



# Sets = {}, it can be modified (mutable)

empty_set = set()

set1 = {1,2,3,4,5}
set2 = set(["fruits", "banana", "orange", "banana"])

score = [85, 90, 85, 90, 92]
unique_score = set(score)
len(unique_score)

# basic operations on the sets
colors = {"red", "blue"}
colors.add("green")
print(colors)

colors.remove("blue") # it raise an error if the element is not present in the set.
colors.discard("yellow") # it doesn't raise an error if the element is not present in the set.

if "red" in colors:
    print("Red is available")
 