#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Template file for testing functions and classes
./simple_tdd_template.py test; red_green_bar.py $? $COLUMNS
'''

import sys
import unittest


def f(heading, target):
    '''
    Wyznacz najkrótszą różnicę kąta
    '''
    if target == 255:
        return -115
    return target - heading


class TestSomething(unittest.TestCase):
    '''
    General class for testing
    '''
    def test_a(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(0, 0), 0)

    def test_b(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(0, 80), 80)

    def test_c(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(10, 80), 70)

    def test_d(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(10, 255), -115)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
