#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:48:21 2021

@author: amalieduejensen
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from math import exp, sqrt
import matplotlib.pyplot as plt

BLOCK_SIZE = 16
ell = 2**8 # number of tables
l = 24 # key length (the last 128 - 24 bits are zeros)


#%% Plot of success probability as a function of m

def P(m):
    t= 2**l / (ell*m)
    
    return 1 - exp(-sqrt(2*m*ell**2/ (2**l) ) * (exp(sqrt(2*m*t**2 / (2**l) )) - 1) / (exp(sqrt(2*m*t**2 / (2**l) )) + 1))


DP=[0]*1000

for m in range(1,1001):
    DP[m-1]=P(m)
    
plt.plot(DP,'-',color='blue')   
plt.xlabel('m') 
plt.ylabel('Success probability p') 


#%%

# the IV is fixed to something random
IV = get_random_bytes(16) 

# this function was given in a previous lecture
def pkcs7_pad(message: bytes, bytes_per_block: int) -> bytes:
    """Return the message padded to a multiple of `bytes_per_block`."""
    if bytes_per_block >= 256 or bytes_per_block < 1:
        raise Exception("Invalid padding modulus")
    remainder = len(message) % bytes_per_block
    padding_length = bytes_per_block - remainder
    padding = bytes([padding_length] * padding_length)
    return message + padding


def f(k: bytes, i: int) -> int:
    """The f function used to create the Hellman tables. The function takes as input the key k
    and the table number i. The table number i is added within the function which means that a
    new function is used for each table."""
    
    # the plaintext is fixed to something random
    plaintext = b"SXQncyBiZWV"
    cipher = AES.new(k, AES.MODE_CBC, IV)
    
    # plaintext is padded and encrypted. Afterwards, the ciphertext is added with the table number
    # i and is then reduced modulo 2**24
    plaintext = pkcs7_pad(plaintext, BLOCK_SIZE)
    ciphertext = cipher.encrypt(plaintext)
    return (int.from_bytes(ciphertext, byteorder='little') + i ) % 2**24


#%% Hellman

# the parameters M and T are fixed to appropriate values
M=89
T=737

# the key-column for each table
K = [[] for i in range(ell)]

# starting values in each table are randomly chosen
for i in range(ell):
    for m in range(M):
        k = get_random_bytes(3) + bytes(13)
        K[i].append(k)


values_in_table = [[] for i in range(ell)]
values_after_t_columns = [[] for t in range(T)]
found_values = []
data_points = []

        
for t in range(1,T):
    print("columns", t)
    for i in range(ell):
        for m in range(M):
            k = f(K[i][m], i)
            values_after_t_columns[t].append(k)
            k = k.to_bytes(16, byteorder="little")
            K[i][m] = k
            
#%%
for t in range(T):
    print("columns", t)
    found_values = found_values + values_after_t_columns[t]
    allvalues = list(set(found_values))
    data_points.append(len(allvalues))
            

#%%

observed_probabilities = [0] * T

for t in range(T):
    observed_probabilities[t] = data_points[t] / 2**24

plt.plot(observed_probabilities,'-',color='red')   
plt.xlabel('t') 
plt.ylabel('point coverage') 
plt.title('Point coverage in practice')


#%% Compute the theoretical success probabilities with t as input and with fixed m = 89

def PT(t):
    m=89
    
    return 1 - exp(-sqrt(2*m*ell**2/ (2**l) ) * (exp(sqrt(2*m*t**2 / (2**l) )) - 1) / (exp(sqrt(2*m*t**2 / (2**l) )) + 1))


theoretical_data_points = [0] * T

for t in range(1,T+1):
    theoretical_data_points[t-1] = PT(t)

plt.plot(theoretical_data_points,'-',color='blue')   
plt.xlabel('t') 
plt.ylabel('success probability p') 
plt.title('Theoretical point coverage')    

#%% Plot the difference between the theoretical and the practical success probabilities  
    
diff = [0] * T

for t in range(T):
    diff[t] = abs(theoretical_data_points[t] - observed_probabilities[t])
    
    
plt.plot(diff,'-',color='green')   
plt.xlabel('t') 
plt.ylabel('Difference') 
plt.title('Absolute difference between theoretical and practical success probabilities')


#%%

            
