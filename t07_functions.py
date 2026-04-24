# Function in python

# Here is how we define a function 
def greet():
    print("Hello")
    print("Hello Again!!")

greet()


# if we are not returning any thing form the function then we can write "pass" or don't write anything
def greet_return():
    print("Hello")
    print("Hello from the return function that return nothing!!")
    pass

greet_return()

# function name must be defining the function work

def calculate_total():
    pass

def send_email():
    pass

def save_password():
    pass


# calling function multiple times

def say_goodbye():
    print("Good Bye!!!")
    print("See You Later!!!")
    pass

say_goodbye()
say_goodbye()
say_goodbye()


# Functions with logic

def check_weather():
    temperature = 34
    if(temperature >= 30):
        print("It's hot!!")
    else:
        print("Nice weather!!")
    
    pass

check_weather()

# Parameters in Function

def greet(name):
    print(f"Hello, {name}")
    print("How are you?")
    pass

greet(name = "Veer raj")
greet("Priyanshu raj")

def greet_fullname(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")
    pass

greet_fullname("Priyanshu", "Gupta")
greet_fullname("Raj", "Priyanshu")
greet_fullname(last_name="Raj", first_name="Priyanshu")
greet_fullname(last_name="Kumar",first_name="Sohan")

# Default Parameters of a function 
def greet_default_lastname(first_name, last_name="Kumar"):
    print(f"Hello, {first_name} {last_name}")
    pass

greet_default_lastname("Priyanshu")
greet_default_lastname("Priyanshu", "Raj")


def calculate_total(amount, tax_rate, discount):
    tax = amount * tax_rate
    final_amount = amount + tax - discount
    print(f"Total : Rs. {final_amount}")

calculate_total(100, 0.08, 10)
calculate_total(amount=100, tax_rate= 0.1, discount=33)


# getting results from functions

def print_sum(a, b):
    print(a+b)
    pass

print_sum(3,4)


def return_sum(a, b):
    return a+b

ans = return_sum(3,4)


if(return_sum(4,7) > 10):
    print("Sum is greater then 10.")


# returning more then one values form a function
def simple_fun():
    lst = [1,2,3,4,5,6]
    first_num = lst[0]
    last_num = lst[-1]
    sum = 0
    for i in lst:
        sum += i
    return first_num, last_num, sum

f, l, sum = simple_fun()
print(f, l, sum)