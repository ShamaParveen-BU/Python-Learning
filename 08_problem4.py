# 4. Replace the double space from problem 3 with single spaces.

string = input("Enter a string: ")

new_string = string.replace("  ", " ")

print("Updated string:")
print(new_string)

# Example:
# Input: I love  Python
# Updated string:
#I love Python

# Alternative Short Solution:
string = "Python  is  awesome"
print(string.replace("  ", " "))

# NOTE: replace(" ", " ") replaces all occurrences of double spaces in the string with single spaces.