#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:48:21 2021

@author: amalieduejensen
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


ell = 2**8 # number of tables
l = 24 # key length (the last 128 - 24 bits are zeros)

BLOCK_SIZE = 16 # number of bytes in AES encryption
IV = get_random_bytes(16) # defining the IV used in AES CBC-mode

def main():
    """Create Hellman tables and compute coverage in the tables."""
    # the following values for M and T have been chosen
    M = 89
    T = 737
    
    #assert 2**l == M * T * ell    
    coverage = coverage_in_hellman_tables(M, T)
    print(coverage)


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



def coverage_in_hellman_tables(M: int, T: int) -> list:
    """Construct Hellman tables and compute coverage. The tables are constructed
    simultaneously, i.e. first the first column of each table is constructed, then
    the second of each table is constructed, ect. Note that the new column overwrites
    the previous column which means that we only store one column for each table at 
    a time."""
    # the key-column for each table
    K = [[] for i in range(ell)]

    # starting values in each table are randomly chosen
    for i in range(ell):
        for m in range(M):
            k = get_random_bytes(3) + bytes(13)
            K[i].append(k)

    values_after_t_columns = [[] for t in range(T)] # contains the values in all tables
    # after computing t columns
    found_values = [] # combining the values in all tables after computing t columns,
    # duplicates are removed
    coverage_size = [] # the coverage size after computing t columns

        
    for t in range(1,T): # construct one column in each table before moving on to next
        # column
        #print("Current number of columns: ", t)
        for i in range(ell):
            for m in range(M):
                k = f(K[i][m], i) # compute next value
                values_after_t_columns[t].append(k)
                k = k.to_bytes(16, byteorder="little") # convert key to bytes such that 
                #it works as input in next iteration
                K[i][m] = k # overwrite previous key
            
    for t in range(T):
        #print("Current number of columns: ", t)
        found_values = found_values + values_after_t_columns[t]
        all_values = list(set(found_values)) # remove duplicates
        coverage_size.append(len(all_values)) # construct list of coverage sizes
        
    return coverage_size
        
        
if __name__ == "__main__":
    main()

