#type() Function and Typecasting

# NOTE:type() function is used to find the data type of a given variable in python.
a = 31 
type (a)
print(type(a))
b = 45.96
type (b)
print (type(b))

# NOTE:A number can be converted into a string and vice versa (if possible)
# #There are many functions to convert one data type into another.

c = "33.78"
type (c)
print (type(c))

#conversion from string to float (Typecasting)

d = float (c) # c but type should be float 
t = type(d)
print(t)

#there are many function to convert one data type into another.
# For example...
e = str (31)
print(str(31))
print (type(e))
print(int("31"))
print(float(31))