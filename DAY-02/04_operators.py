# Operators in Python

#01_Arithmetic operators: +, -, *, / etc.

a = 2 
b = 3 
c = a+b 
print (a+b)

#02_Assignment operators: =, +=, -= etc.

a = 6-4 # Assign 6-2 in a
print (a)
b = 6 
b += 7 # increase the value of b by 7 and then assign it to b
print (b)
b = 6
b -= 5 # decrease the value of b by 5 and then assign it to b
print (b)

 #03_Comparison operators: ==, >, >=, <, != etc.
 #_FACTZZZ:*Comparing things  ==, >, >=, <, != etc. ALWAYS gives True or False.

a = 5<3 
print (a) 
b = 5>= 3 
print (b)

#04_Logical operators: and, or, not.

# Truth Table for OR Operator

print("A\tB\tA or B")
print(True, "\t", True, "\t", True or True)
print(True, "\t", False, "\t", True or False)
print(False, "\t", True, "\t", False or True)
print(False, "\t", False, "\t", False or False)

# Truth Table for AND operator 

print("A\tB\tA and B")
print(True, "\t", True, "\t", True and True)
print(True, "\t", False, "\t", True and False)
print(False, "\t", True, "\t", False and True)
print(False, "\t", False, "\t", False and False)

# Truth Table for NOT Operator

print("A\tNot A")
print(True, "\t", not True)
print(False, "\t", not False)

