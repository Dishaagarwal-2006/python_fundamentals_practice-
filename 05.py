# ✅ Q4. Smart Swap & Financial Calculator

# Ask user for:

# Two numbers a and b (string input)

# Convert them to float

# Swap them without using a third variable

# Then ask for:

# Principal, Rate, Time (string inputs)

# Convert them to float and calculate:

# SI = (P * R * T) / 100


# Print:

# Swapped values

# Simple Interest

# Total Amount = P + SI

a = float(input("enter the number:"))
b = float(input("enter the number:"))
a ,b = b,a 
print("after swapping :" , a , b )
p = float(input("enetr the numbers:"))
r = float(input("enetr the numbers:"))
t = float(input("enetr the numbers:"))
SI = (p*r*t)/100
print(SI)
print("toatal amount:", p + SI)