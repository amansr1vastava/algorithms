# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while left<=right:
        mid = (right + left) // 2
        if (x == a[mid]):
            return mid
        if x < a[mid]:
            right = mid-1
        if x > a[mid]:
            left = mid + 1
    return -1

data = list(map(int, input().split()))
n = data[0]
m = data[1:]
toFind = list(map(int, input().split()))
k = toFind[0]
a = toFind[1:]
for i in a:
    print(binary_search(m,i),end = ' ')
