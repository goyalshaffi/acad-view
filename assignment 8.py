
 # q1
'''
Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
Index 	Field 	Values
0 	4-digit year 	2008
1 	Month 	1 to 12
2 	Day 	1 to 31
3 	Hour 	0 to 23
4 	Minute 	0 to 59
5 	Second 	0 to 61 (60 or 61 are leap-seconds)
6 	Day of Week 	0 to 6 (0 is Monday)
7 	Day of year 	1 to 366 (Julian day)
8 	Daylight savings 	-1, 0, 1, -1 means library determines DST
'''
 # q2
'''
import time
print(time.asctime(time.localtime()))



# q3
from datetime import date
d=date.today()
print(d.month)

# q4


from datetime import date
d=date.today()
print(d.day)
'''
# q5
from datetime import date
d1=datetime.date.today()
d1.strftime("%d%m%y")
print(d1.day)


'''
# q6

import time
print(time.localtime())




# q7


import math
n=int(input("enter no"))
print(math.factorial(n))


 # q8


import math
a=int(input("enter value"))
b=int(input("enter value"))
print(math.gcd(a,b))


# q9


import os
print(os.getcwd())
print(os.environ)
'''
