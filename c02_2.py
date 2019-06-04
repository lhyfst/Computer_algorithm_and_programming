# -*- coding:utf-8 -*-

"""
本程序在Ubuntu Python2.7环境下通过测试

Problem:
Realize the bubble sort algorithm in python.
"""

completed = False

input_list = [3,2,5,9,8,4]
length = len(input_list)

while not completed:
    completed = True
    for idx in range(length-1):
        if input_list[idx] > input_list[idx+1]:
            completed = False
            input_list[idx],input_list[idx+1] = input_list[idx+1],input_list[idx]

print input_list