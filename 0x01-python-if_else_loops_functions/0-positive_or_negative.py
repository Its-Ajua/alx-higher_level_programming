#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
   print("{} number is positive".format(number))
elif number == 0:
   print("{} number is zero".format(number))
else:
   print("{} number is negative".format(number))
=======
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
>>>>>>> a9448772e40e3f4501309353b2657e6299d8522f
