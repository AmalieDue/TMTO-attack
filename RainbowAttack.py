#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:39:32 2021

@author: andershartmann
"""

#Import useful packages to perform AES encryption
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


IV = get_random_bytes(16) #Definng the IV used in AES CBC-mode
BLOCK_SIZE = 16 #Defining the block size


def main():
    """Create rainbow table and compute coverage in the table."""
    #Defining the final dimension of the rainbow table
    m_fin=2**8
    t_fin=500
    
    #assert 2**l == m_fin * t_fin * ell    
    coverage = coverage_in_rainbow_table(m_fin, t_fin)
    print(coverage)



#Defining a padding function used for AES.
    #Input: A message and a blocksize
    #Output: Padded message
def pkcs7_pad(message: bytes, bytes_per_block: int) -> bytes:
    """Return the message padded to a multiple of `bytes_per_block`."""
    if bytes_per_block >= 256 or bytes_per_block < 1:
        raise Exception("Invalid padding modulus")
    remainder = len(message) % bytes_per_block
    padding_length = bytes_per_block - remainder
    padding = bytes([padding_length] * padding_length)
    return message + padding


#Defining the round function used in the i'th column
    # Input: A key k and the current column index i
    # Output: The value of the roundfunction used on the ciphertext of the known plaintext.
def f(k, i):
    #plaintext = b"It's been a hard day's night, and I've been working like a dog"
    plaintext = b"SXQncyBiZWV"
    cipher = AES.new(k, AES.MODE_CBC, IV)
    plaintext = pkcs7_pad(plaintext, BLOCK_SIZE)
    ciphertext = cipher.encrypt(plaintext)
    return (int.from_bytes(ciphertext, byteorder='little') + i ) % 2**24


def coverage_in_rainbow_table(m_fin: int, t_fin: int) -> list:
    #Defining the starting values in the rainbow table. 
    K=[]
    for i in range(m_fin*t_fin):
        k= get_random_bytes(3) + bytes(13)
        K.append(k)
    
    
    #Defining list to contain results
    Data_points=[]  #Contains the coverage after each addition of a column
    Found_values=[] #Contains the found points 
    key_list=[] # Contains the keys that need to be used to create a new column in the rainbow table.


    #Creating the rainbow table
    for i in range(t_fin): 
        print(i)
    
        #Creating a new column in the rainbow table
        for j in range(m_fin*t_fin): 
            k=f(K[j],i)
            key_list.append(k)
            k = k.to_bytes(16, byteorder="little")
            K[j]=k
    
        #Keep track of what key-values have been found and removing duplicate values
        Found_values=Found_values+key_list #Defines all found values
        allvalues=list(set(Found_values)) #removes duplicate values
        Data_points.append(len(allvalues)) # Calculate the number of different key-values found.
        key_list=[] #reseting the key list.
        
    return Data_points







