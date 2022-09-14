

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
algo:1) Frequency count of A
     2) if a occurces odd time return this value
'''

from collections import Counter
def solution(A):
    # write your code in Python 3.6
    c = Counter(A)
    #   ls = []
    for i in c.keys():
        # print(i, c[i])
        if c[i] &1 == 1:
            return i
