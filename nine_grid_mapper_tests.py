#!/usr/bin/env python
# encoding: utf-8
import itertools
import unittest
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
        self.assertEqual(encoded_hash, 268435455)    

    def test_encode_no_hash_collisions(self):
        # for all possible grids that can be created, no two should have
        # the same hash
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
        print '\n'
        for i in xrange(1, len(pairs)+1):
            print 'Combination round %d of %d' % (i, len(pairs))
            grid = [list(x) for x in itertools.combinations(pairs, i)]
            all_grids.extend(grid)
        hashes = []
        for grid in all_grids:
            hashes.append(self.grid.encode_hash(grid))
        self.assertEqual(len(hashes), len(set([tuple(h) for h in hashes])))

    ''' Example Tests
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
    '''

if __name__ == '__main__':
    unittest.main()