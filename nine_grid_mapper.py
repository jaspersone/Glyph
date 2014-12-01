#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import pprint

class NineGridMapper:
    def __init__(self):
        ''' Setups up a mapping of key values to our internal
            numbering system as shown in the following grid.
            
            The grid is a nine dotted grid, where the verticies
            are label as numbers from 1 - 9:
            
            1 2 3
            4 5 6
            7 8 9
            
            The below shows potential edges that can be formed
            between verticies. Please note the basic rules:
                1. There exist no edge that connects a vertex
                   to itself
                2. There exist no edge that connects more than
                   two verticies at one time
                3. We describe edges as two number the start and
                   the end of the line, where the start number
                   is strictly less than the ending number.
                4. x's represent keys that are not valid
            
            Table of Indexes based upon vertex pairs
                1   2   3   4   5   6   7   8   9
               ___________________________________
            1 | x   0   x   1   2   3   x   4   x
              |     
            2 | x   x   5   6   7   8   9   x   10
              |         
            3 | x   x   x   11  12  13  x   14  x
              |
            4 | x   x   x   x   15  x   16  17  18
              |
            5 | x   x   x   x   x   19  20  21  22
              |
            6 | x   x   x   x   x   x   23  24  25
              |
            7 | x   x   x   x   x   x   x   26  x
              |
            8 | x   x   x   x   x   x   x   x   27
              |
            9 | x   x   x   x   x   x   x   x   x
        '''
        # max_hash = 2^0 + 2^1 + 2^2 + ... 2^27
        self.max_hash = 268435455
        self.grid = [
                    (1,2), (1,4), (1,5), (1,6), (1,8),
                    (2,3), (2,4), (2,5), (2,6), (2,7), (2,9),
                    (3,4), (3,5), (3,6), (3,8),
                    (4,5), (4,7), (4,8), (4,9),
                    (5,6), (5,7), (5,8), (5,9),
                    (6,7), (6,8), (6,9),
                    (7,8),
                    (8,9),
                    ]

    def encode_hash(self, pairs):
        ''' A basic function that hashes a list of vertex pairs
            into a unique integer.
            
            The basic algorithm is takes a given list of vertices (keys)
            and assigns each pair a power of two.
            
            return: a unique integer which represents the state of the
                    nine dot grid that the user has passed to encode_hash
        '''
        # ensures no duplicate vertex pairs
        keys = list(set(pairs))
        hashed_result = 0
        for key in keys:
            try:
                hashed_result += 2 ** self.grid.index(key)
            except Exception as e:
                ''' if an exception is thrown, it is likely due to the fact
                    that a key of vertex pairs that was passed to encode_hash
                    does not exist inside of self.grid.
                '''
                print e
                return None
        return hashed_result
    
    def decode_hash(self, hashed_key):
        ''' params: hashed_key is an integer between 0 and self.max_hash
            return: an list of edges described as (V1,V2)
        '''
        if type(hashed_key) is not int or 
            hashed_key > self.max_hash or
            hashed_key < 0:
            return None
        # create binary version of number (prefilled to a length of 28 chars)
        binary = bin(hashed_key)[2:].zfill(28)
        last_index = len(binary) - 1
        result = []
        for x in xrange(len(binary)):
            if binary[last_index - x] is '1':
                results.append(self.grid[x])
        return result
    
def main():
    my_mapper = NineGridMapper()
    pprint.pprint(my_mapper.grid)

def test():
    # TODO: call tests here
    print 'Running tests.'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
