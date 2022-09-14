# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

  '''
  Algo:1) N --> bin = num
       2) remove 0 from start and end using strip('0')
       3) split this binary number using split('1')
       4) return the max len of 0's
  '''

def solution(N):
    # write your code in Python 3.6
    # print(bin(N)) # output: 0b101
    num = bin(N)[2:].strip('0').split('1')
    return max([len(x) for x in num])


  
