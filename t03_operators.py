# Operators in pythos
# (1) Arithematic Operators (t00_intfloat.py)
# (2) Comparision Operators (t02_booleans.py)
# (3) Logical Operators

age = 25
has_license = False
long_dash = "-" * 50
# AND - both of the condition must be true
can_drive = age >= 16 and has_license
print(can_drive)

# OR - at least one condition must be true
can_drive = age >= 16 or has_license
print(can_drive)

# NOT - reverse the value
can_drive = age >= 16 or has_license
print(not can_drive) # not True = False
print(long_dash)

print(True and True)
print(True and False)
print(False and False)
print(long_dash)

print(True or True)
print(True or False)
print(False or False)
print(long_dash)

print(not True)
print(not False)
print(long_dash)


# Increment and Decrement operator
score = 23
score = score + 5
score += 5