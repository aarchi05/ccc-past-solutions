#**********
#Author: aarchi05
#CCC 2011: J2 - Who Has Seen The Wind?
#**********

import math
h = int(input())
M = int(input())

t = 1
A = -6*(math.pow(t, 4)) + h*(math.pow(t, 3)) + 2*(math.pow(t, 2)) + t

while t < M and A > 0:
    t += 1
    A = -6 * (math.pow(t, 4)) + h * (math.pow(t, 3)) + 2 * (math.pow(t, 2)) + t
if A > 0:
    print("The balloon does not touch the ground in the given time.")
else:
    print("The balloon first touches ground at hour: ", t)






    

