import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagsum1=diasum2=0
    for i in range (0,len(arr)):
        for j in range (0,len(arr)):
            if i==j:
                diagsum1+=arr[i][j]
            if i+j==len(arr)-1:
                diasum2+=arr[i][j]
    return(abs(diagsum1-diasum2))
    # Write your code here

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
