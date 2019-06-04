# -*- coding:utf-8 -*-

"""
本程序在Ubuntu Python2.7环境下通过测试

Problem:
Test the Goldbach’s conjecture using python to output all possible solutions for an even number 2<N<10000, where both a and b are primes and a+b=N.
"""

from c02_1 import find_all_prime_nums
import numpy as np

all_primes = np.array(find_all_prime_nums(N=10000))
all_evens = np.arange(4,10000,2)


def test_a_even(even_num):
    possible_solutions = []
    my_primes = all_primes[all_primes<even_num]
    for prime_1 in my_primes[my_primes<=even_num/2]:
        prime_2 = even_num - prime_1
        if prime_2 in my_primes:
            possible_solutions.append([prime_1,prime_2])
    if not possible_solutions:
        print "find a counter-example " + str(even_num)
        raise
    return possible_solutions

all_possible_solutions = []
for even_num in all_evens[:10000]:
    all_possible_solutions.append(test_a_even(even_num))
print 'The Goldbach’s conjecture has been proved when the even number less than 10000. \n All solutions have been stored in the list all_possible_solutions'