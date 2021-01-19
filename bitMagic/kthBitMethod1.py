"""
Method 1: Using left shift operator
Algorithm:
  Step 1: Left Shift given number 1 by k-1 to create a number that has only set bit as kth bit. (temp = 1 << (k-1)
  Step 2: (n & temp) == 0       ---> kth bit is unset
          (n & temp) != 0       ---> kth bit is set
          
EX: 
n = 27 k = 4
(27) = (11011)
initially, temp = 1, after we do temp = 1 << (k-1) 
temp = 1000
  11011   (n)
&  1000   (temp)
=========
  01000     (SET)
"""

n, k = map(int, input().split())        # n --> number to check     k --> check for bit
temp = 1
temp = 1 << (k-1)
if n & temp == 0:
    print("UNSET")
else:
    print("SET")

    
"""
OP:
5 1
SET
"""
