#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
对arr去重并获取最大值
'''

def getMax(arr):
    set1 = set(arr)
    print("sorted: ", set1)
    tmp = 0
    for i in set1:
        tmp = i
        for j in set1:
            if j > tmp:
                tmp = j
    return tmp

if __name__ == '__main__':
    arr = [1, 2111, 3, 33, 2]
    print("max: ", getMax(arr))