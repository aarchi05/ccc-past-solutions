#**********
#Author: aarchi05
#CCC 2012: J3 - Icon Scaling
#**********

k = int(input())

s = ""
x = ""
space = " "

for i in range(k):
     s = s + "*"
     x = x + "x"
     space = space + " "
for i in range(k):
    print(s + x + s)
for i in range(k):
    print(space + x + x)
for i in range(k):
    print(s + space + s)