"""
METHOD 2: Using the right shift
Algorithm:
  Step 1: Right shift n by k-1 (n >> (k-1))
  Step 2: if last bit is 1, then kth bit is SET else NOT SET
  
EX:
n = 27 k = 4
(27) = (11011)
n >> k-1 = 27 >> 3 = 00011
and finally, 
((00011)&1) to check if kth bit is set or not
"""

n, k = map(int, input().split())
n = n >> (k-1)
if (n & 1) == 0:
  print("UNSET")
else:
  print("SET")
  

