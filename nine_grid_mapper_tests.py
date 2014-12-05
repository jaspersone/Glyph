#!/usr/bin/env python
# encoding: utf-8
import itertools
import unittest
import pprint
from nine_grid_mapper import NineGridMapper

class nine_grid_mapper_tests(unittest.TestCase):
    def setUp(self):
        self.grid = NineGridMapper()
    
    def test_encode_no_pairs(self):
        # an empty 9-grid should return a hash of 0
        pairs = []
        encoded_hash = self.grid.encode_hash(pairs)
        self.assertEqual(encoded_hash, 0)

    def test_encode_simple_case(self):
        # a grid with edges (1,2) and (1,4) should return a hash of 3
        pairs = [(1,2), (1,4)]
        encoded_hash = self.grid.encode_hash(pairs)
        self.assertEqual(encoded_hash, 3)

    def test_encode_simple_case_reversed_pairs(self):
        # a grid with edges (1,2) and (1,4) should return a hash of 3
        pairs = [(1,4), (1,2)]
        encoded_hash = self.grid.encode_hash(pairs)
        self.assertEqual(encoded_hash, 3)

    def test_encode_illegal_pair(self):
        # a grid with edges (1,2) and (1,3) contains an illegal pair
        # and should return None, as do other list of pairs that
        # contain illegal pairs
        pairs = [(1,2), (1,3)]
        encoded_hash = self.grid.encode_hash(pairs)
        self.assertEqual(encoded_hash, None)
    
    def test_encode_full_grid(self):
        # a grid with all possible edges should return a hash of 268435455
        pairs = [
                (1,2), (1,4), (1,5), (1,6), (1,8),
                (2,3), (2,4), (2,5), (2,6), (2,7), (2,9),
                (3,4), (3,5), (3,6), (3,8),
                (4,5), (4,7), (4,8), (4,9),
                (5,6), (5,7), (5,8), (5,9),
                (6,7), (6,8), (6,9),
                (7,8),
                (8,9),
                ]            
        encoded_hash = self.grid.encode_hash(pairs)
        self.assertEqual(encoded_hash, self.grid.max_hash)    

    def test_decode_hash_is_0(self):
        hashed_key = 0
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(len(pairs), 0)

    def test_decode_hash_is_1(self):
        hashed_key = 1
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(pairs, [(1,2)])

    def test_decode_hash_is_3(self):
        hashed_key = 3
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(pairs, [(1,2),(1,4)])
    
    def test_decode_hash_is_268435455(self):
        hashed_key = 268435455
        expected = [
                (1,2), (1,4), (1,5), (1,6), (1,8),
                (2,3), (2,4), (2,5), (2,6), (2,7), (2,9),
                (3,4), (3,5), (3,6), (3,8),
                (4,5), (4,7), (4,8), (4,9),
                (5,6), (5,7), (5,8), (5,9),
                (6,7), (6,8), (6,9),
                (7,8),
                (8,9),
                ] 
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(pairs, expected)
    
    def test_decode_illegal_hash_low(self):
        hashed_key = -1
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(pairs, None)

    def test_decode_illegal_hash_high(self):
        hashed_key = 268435456 # == 2^28 (one larger than max hash)
        pairs = self.grid.decode_hash(hashed_key)
        self.assertEqual(pairs, None)

    ''' DO NOT run this test, unless you want your machine to run out of memory
    def test_encode_no_hash_collisions(self):
        # for all possible grids that can be created, no two should have
        # the same hash
        # NOTE: this is a long running test, really long running!
        pairs = [
                (1,2), (1,4), (1,5), (1,6), (1,8),
                (2,3), (2,4), (2,5), (2,6), (2,7), (2,9),
                (3,4), (3,5), (3,6), (3,8),
                (4,5), (4,7), (4,8), (4,9),
                (5,6), (5,7), (5,8), (5,9),
                (6,7), (6,8), (6,9),
                (7,8),
                (8,9),
                ]
        all_grids = []
        
        import datetime
        print '\n'
        for i in xrange(1, len(pairs)+1):
            start = datetime.datetime.now()
            grid = [list(x) for x in itertools.combinations(pairs, i)]
            all_grids.extend(grid)
            end = datetime.datetime.now()
            print 'Combinations round %d of %d ran in %f secs.' % (i, len(pairs), (end - start).total_seconds())

        hashes = []
        for grid in all_grids:
            hashes.append(self.grid.encode_hash(grid))
        self.assertEqual(len(hashes), len(set([tuple(h) for h in hashes])))
    '''
    
    def test_generate_oracle(self):
        filename_out = 'oracle.txt'
        pairs = [
                (1,2), (1,4), (1,5), (1,6), (1,8),
                (2,3), (2,4), (2,5), (2,6), (2,7), (2,9),
                (3,4), (3,5), (3,6), (3,8),
                (4,5), (4,7), (4,8), (4,9),
                (5,6), (5,7), (5,8), (5,9),
                (6,7), (6,8), (6,9),
                (7,8),
                (8,9),
                ]
        all_grids = []
        
        import datetime
        print '\n'
        for i in xrange(1, 5):
            start = datetime.datetime.now()
            grid = [list(x) for x in itertools.combinations(pairs, i)]
            all_grids.extend(grid)
            end = datetime.datetime.now()
            print 'Generate oracle round %d of %d ran in %f secs.' % (i, len(pairs), (end - start).total_seconds())
        print 'Processing %d grids...' % len(all_grids)
        
        with open(filename_out, 'w') as f:
            for line in all_grids:
                f.write(self.convert_to_csv_line(line))
                f.write('%d\n' % self.grid.encode_hash(line))
        
    def convert_to_csv_line(self, line):
        return '%s\n' % (','.join(['%d%d' % x for x in line]))

if __name__ == '__main__':
    unittest.main()