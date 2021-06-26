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
    heading = heading % 360
    result = target - heading
    if result > 180:
        result = result - 360
    elif result < 0:
        result = result + 360
    if result > 180:
        result -= 360
    return result


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

    def test_e(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(360, 0), 0)

    def test_f(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(255, 10), 115)

    def test_g(self):
        '''
        TestSomething:
        '''
        self.assertEqual(f(10, -60), -70)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
