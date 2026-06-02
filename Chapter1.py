print("Hello,Shama")
#practice Q.01 write a program to print "Twinkle Twinkle Little Star" in python.
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.""")
#practice Q.02 print the table of 5.
print("""5*1=5
 5*2=10
 5*3=15
 5*4=20
 5*5=25
 5*6=30
 5*7=35
 5*8=40
 5*9=45
 5*10=50""")

#practice Q.03 Install an external module and use it to perform an operation of your interest.

import pyttsx3
engine = pyttsx3.init()

engine.say("Consistency is the key to success")

engine.runAndWait()

#practice Q.04 Write a python program to print the contents of a directory using the os module. 
import os

contents = os.listdir()

for item in contents:
    print(item)
    
