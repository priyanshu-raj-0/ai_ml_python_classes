
# errors



# if x > 13  # syntax error
#     print("tum dum tadaoo..")


# if x > 13:  # name error
#     print("main kya ladle meoww.")


# result = 10 / 0     # zero division error


# print(x)  # name error


# "hello" + 5   # Type error

# ---------------------------------------------------------------------------



# try and except in python

def risky_operation(num):
    return 100 / num

try:
    ans = risky_operation(0)
    print(ans)
except:
    print("Error accured in this code!!")



# ex:-
try:
    age = int(input("Enter your age: "))
    print(f"After 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")

# ex:-
try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")



# ---------------------------------------------------------------------------


# try, except and else

try:
    ans = risky_operation(10)

except:
    print("Error accured in this code!!")

else:
    print(f"The answer is : {ans}")
    print("This is else block that runs when the try block successfully runs.")



# ex:-
try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")




# ---------------------------------------------------------------------------


# try, except and finally

try:
    ans1 = risky_operation(10)
    print("Answer is :", ans1)
except:
    print("Error accured in this code!!")
finally:
    print("finally block is used for clean up program.")
    print(f"This block always run either the try fails or not!!")

# ex:-
try:
    file = open('data.txt', 'r')    # First create data.txt then run this code.
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")




# ---------------------------------------------------------------------------



# most important this of this topic by gemini


import requests

try:
    # 1. Only put the "risky" network call here
    response = requests.get("https://example.com", timeout=5)   # timeout=5 is explained in the bottom of the program
    response.raise_for_status()                                 # Raises an error if the status is 4xx(404 not found error) or 5xx (500 server error)

except requests.exceptions.RequestException as e:
    # 2. Catch network issues, timeouts, or 404s/500s here
    print(f"API Error: {e}")

else:
    # 3. SUCCESS! Put all your logic/processing here
    data = response.json()
    print("Processing data:", data)

finally:
    # 4. Cleanup (if needed)
    print("Finished attempt.")


"""

timeout=5

The timeout=5 parameter in the requests library is a safety limit that tells your program how long to wait for the server before giving up. 
Without this, if an API server is down or extremely slow, your script could hang indefinitely, "staring into the void" and blocking the rest of your code from running. 

What exactly does it do?

The 5-Second Rule: It tells Python to wait a maximum of 5 seconds for the server to respond.
Two-in-One: By providing a single number, it sets a 5-second limit for both establishing a connection and waiting for the first byte of data.
Error Handling: If the 5 seconds pass without a response, it raises a requests.exceptions.Timeout error, which you can then catch in your except block to handle gracefully. 

Advanced Tip: Splitting the Time : If you want to be more specific, you can pass a tuple to set different limits for connecting vs. reading data: 

python
# Wait 3s to connect, but give the server 10s to actually send the data
response = requests.get(url, timeout=(3, 10))  Use code with caution.

Connect Timeout: Time spent trying to "shake hands" with the server.
Read Timeout: Time spent waiting for the server to start sending the actual response.





response.raise_for_status()

In the requests library, response.raise_for_status() is a built-in method that checks the HTTP Status Code of the server's response.
Normally, if an API call "fails" (like a 404 Not Found or a 500 Server Error), Python won't actually crash. It will just give you a response object with that error code, and your code will keep running—which can lead to weird bugs later when you try to process empty data.

What it does:
Success (2xx): If the code is 200 (OK), it does nothing and moves to the next line.
Failure (4xx or 5xx): If the server says "Client Error" (4xx) or "Server Error" (5xx), it forcefully raises an exception.

Why use it?
It forces your code into the except block immediately if the API didn't return what you wanted.

Without it:
response = requests.get(url)
data = response.json()  # If the site 404s, this might crash with a confusing error


With it:
try:
    response = requests.get(url)
    response.raise_for_status() # Jumps to 'except' if status is 404, 500, etc.
    data = response.json()      # This only runs if the response was 100% healthy
except requests.exceptions.HTTPError as e:
    print(f"The server returned an error: {e}")
    

It's essentially a "safety gate" that ensures you only work with good data.
Do you want to see a list of the most common status codes you'll run into while testing APIs?

"""


