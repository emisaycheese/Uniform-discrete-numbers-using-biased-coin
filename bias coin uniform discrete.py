#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:13:17 2019

@author: ruiqianyang
"""

import random

def flipcoin(p):
    if random.uniform(0,1) <= p:
        return 'H'
    else:
        return 'T'

def check(toss): #return s, where n = 2^s*(2t+1)
    if toss == 'HT':
        return 0
    elif toss == 'TH':
        return 1
    else:
        return None

X = None
p = 0.5
print("Coin Toss Sequence: ", end = "")
while X is None:
    toss = flipcoin(p) + flipcoin(p)
    print(toss, end = "")
    X = check(toss)

print("\nX = " + str(X))

#%%
##generate numbers 1-7
#or 1 to n, n will be input
num_toss=0
print('please enter a n:')
n=int(input())
n2=n
while n2//2>0:
    num_toss+=1
    n2=n2//2
num_toss+=1

#this function will check the number corresponding to toss outcome sequence
#based on binary number:
#ex: 'HHH' ->'000'->0
#
#
#

def check(toss):
    binary=''.join('1' if i=='T' else '0' for i in list(toss))
    b=sum([int(binary[i])*(2**(len(binary)-i-1)) for i in range(len(binary))])
    #print(b+1)
    if b+1>n:
        return None   ##discard 8
    return b+1


import random
##bias coin
p=0.3


def unbias_coin(p):
    
    def flip_coin(p):
        a=random.random()
        if a<=p:
            return 'H'
        else:
            return 'T'
    
    while True:
        res=flip_coin(p)+flip_coin(p) 
        if res=='HT':
            return 'H'
        if res=='TH':
            return 'T'
    
  
output=[]    
for i in range(1000):
    X=None
    while X is None:
        toss=''.join(unbias_coin(p) for i in range(num_toss))
        print(toss)
        X=check(toss)
    
    output.append(X)
    print(X)    



#%%

We can us the following code to generate a table of f(n,m)
.

def table(N):
    fold = [1,] #f(0,0) = 1
    print('1')
    for n in range(1, N+1):
        fnew = [1,] #f(n,0) is always 1
        print('1', end=' ')
        for m in range(1, n):
            f = fold[m-1] % 2 + fold[m] % 2 #Apply Thm 1
            fnew.append(f)
            print(str(f), end=' ')
        fnew.append(1) #f(n,n) is always 1
        print('1')
        fold = fnew

table(10)
#%%
By Theorem 1, we know that if f(n,m)=2
, then the last toss of the one valid (n,m)
 sequence is H and the last toss of the other is T. Hence, our more efficient algorithm can be described as follows:

If (km(k))
 is even, then assign X=0
 if the last toss is T. Assign X=1
 if the last toss is H.
If (km(k))
 is odd, then toss another coin and update k
 and m(k)
.
The algorithm can be implemented in the following code:

import random

def flipcoin(p):
    if random.uniform(0,1) <= p:
        return 'H'
    else:
        return 'T'

def factor2(n): #return s, where n = 2^s*(2t+1)
    if n == 0: return 0
    s = 0;
    while n % 2 == 0:
        s = s + 1
        n = n / 2
    return s

p = 0.5
k = 0
m = 0
even = False
print("Coin Toss Sequence: ", end = "")
while even is False:
    toss = flipcoin(p)
    print(toss, end = "")
    k = k + 1
    if toss == 'H':
        m = m + 1
        X = 1
        if factor2(k) - factor2(m) > 0: even = True
    else:
        X = 0
        if factor2(k) - factor2(k-m) > 0: even = True

print("\nX = " + str(X))