# -*- coding:utf-8 -*-

"""
本程序在Ubuntu Python2.7环境下通过测试

Problem:
Find all the prime numbers less than a non-negative integer N.

输入范例：python c02_1.py 20
"""

import sys 



def find_all_prime_nums(N):
    """Find all the prime numbers less than a non-negative integer N."""
    primes = [2]
    num = 3

    while num < N:
        for pri_num in primes:
            if num % pri_num == 0:
                break
        else:
            primes.append(num)
        num += 1
    
    return primes
    
    
if __name__ == "__main__":
    N = int(sys.argv[1])
    primes = find_all_prime_nums(N)
    print primes