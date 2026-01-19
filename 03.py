# ✅ Q2. Scientific Calculator Expression Analyzer

# Ask the user for a number x (string input).

# Compute:

# result = x + 3 * 2 ** 2 - x / 2


# Now:

# Print the result

# Print why ** and * were evaluated before + and - (in comments)

# Print:

# Integer part of result

# Fractional part of result



# SCIENTIFIC CALCULATOR EXPRESSION ANALYZER 
x = float(input("enetr the number:"))
result=x + 3 * 2 ** 2 - x / 2
print(result)
# so ** and * is evaluated before + and - because of precedence they have more precedence than + and - thta swhy ...
integer_part = int(result)
fractional_part = result - int(result)
print("integer part of result : " ,integer_part)
print("fractional part of result : " ,fractional_part )
