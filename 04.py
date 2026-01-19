# ✅ Q3. Temperature + Area + Type Conversion Combo

# Ask user for:

# Temperature in Celsius (string)

# Radius of a circle (string)

# Convert both to float and:

# Convert Celsius → Fahrenheit

# Calculate area of circle using:

# area = 3.14 * r * r


# Print:

# Fahrenheit temperature

# Area of circle

# Their data type

temperature_in_celcius = float(input("enter the number:"))
radius= float(input("enter the number:"))
# F = (C × 9/5) + 32
fahrenheit = (temperature_in_celcius * (9/5)+32)
area = 3.14 * radius * radius 
print(type(fahrenheit))
print(type(area))
print(fahrenheit)
print(area)

