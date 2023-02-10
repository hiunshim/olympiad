import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

#import os
#import sys
#from atexit import register
#from io import BytesIO

#sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
#sys.stdout = BytesIO()
#register(lambda: os.write(1, sys.stdout.getvalue()))

#input = lambda: sys.stdin.readline().rstrip('\r\n')

