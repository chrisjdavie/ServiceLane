'''
Solution to the hackerrank Service Lane Challenge.

https://www.hackerrank.com/challenges/service-lane

Series of integers, find the smallest integer in a segment

Created on 29 Dec 2015

@author: chris
'''

# n - length of array
# t - number of segments 
n,t = map(int,raw_input().strip().split())

# ar - array of integers to be examined
ar = map(int,raw_input().strip().split())

for _ in xrange(t):
    
    # i - start of segment
    # j - end of segment
    i,j = map(int, raw_input().strip().split())
    
    print min(ar[i:j+1])

