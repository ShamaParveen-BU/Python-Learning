# Type Conversion (Typecasting)

# The input() function always returns data as a string. 

a = input("Enter first number:")
b = input("Enter second number:")
print (a+b)

# Here, if the user enters 1 and 2,
# the output will be 12 insead of 3. 
# This happens because a and b are strings. 
# The + operator concatenates strings.

# Correct way: convert the inputs to integers.

a = int(input("Enter first number"))
b = int(input("Enter second number"))

print (a+b)

# Now the + operator performs arithmatic adition.