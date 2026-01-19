# ✅ Q1. Smart User Info & Math Report

# Ask the user for:

# Name (string)

# Age (string input → convert to int)

# Two numbers (string input → convert to float)

# Now print:

# A sentence:

# Hello ___, you will be ___ years old after 5 years.

# Print:

# Sum, difference, product, quotient of the two numbers

# Print the average of all three numbers:
# (age, num1, num2) — all treated as floats

# Print each result with its type

# SMART USER INFO AND MATH REPORT 
name = input("enter your name :")
age = int(input("enter your age :"))
num1 = float(input("enetr the number:"))
num2 =float(input("enter the number:"))
     
print("Hello",name ," you will be", age+5," years old after 5 years.")

print("sum of two numbers :" , num1+num2)
print("difference of two numbers :" , num1-num2)
print("product of two numbers :" , num1*num2)
print("quotient of two numbers :" , num1/num2)

average = float((age+num1+num2)/3)
print( "the average will be :" , average)

print(type(name))
print(type(age))
print(type(num1))
print(type(num2))
print(type(num1+num2))
print(type(num1-num2))
print(type(num1*num2))
print(type(num1/num2))
print(type(average))
