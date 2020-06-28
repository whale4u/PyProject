#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
时间复杂度:O(log2n);
注意：二分查找的前提必须待查找的序列有序。
"""


def BinarySearch(array,t):
    low = 0
    height = len(array)-1
    while low < height:
        mid = (low+height)//2
        if array[mid] < t:
            low = mid + 1

        elif array[mid] > t:
            height = mid - 1

        else:
            return array[mid]

    return -1


if __name__ == "__main__":
    print(BinarySearch([1, 2, 3, 34, 56, 57, 78, 87], 57))