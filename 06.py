# ✅ Q5. Ultimate Number Dissector

# Ask the user for a decimal number as a string, for example:

# "123.456"


# You must:

# Convert it to float

# Extract and print:

# Integer part

# Fractional part

# Convert the number into:

# int

# float

# string

# Print each value and its type

# Also print:

# Square of the number

# Half of the number
dec_num = input("enetr the number:")
float(dec_num)
integer_part = int(dec_num)
fractional_part = dec_num - int(dec_num)

print(type(int(dec_num)))
print(type(float(dec_num)))
print(type(dec_num))

print("square of number :" , dec_num ** dec_num)
print("half of the number:", dec_num/2)

