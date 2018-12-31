#!/bin/python3

N = int(input())

if (N % 2 != 0):
    print("Weird")
else: # Therefore even
    if N in range(2,7):
        print("Not Weird")
    if N in range(6,21):
        print("Weird")
    if N > 20:
        print("Not Weird")
