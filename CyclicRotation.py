# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
algo: 1) first check arr A lenth of ln if ln >0 and K > ln then K = K % ln
      2) arrange this arr
'''

def solution(A, K):
    # write your code in Python 3.6
    ln = len(A)
    if ln >0 and K > ln:
        K = K%ln
    ln_k = ln - K
    C = A[:ln_k]
    B = A[ln_k:]
    BC = B+C
    return BC

    pass
