#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
生成4位数数字验证码
"""

def main():
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    print("%s%s%s%s" % (i, j, k, l))


if __name__ == '__main__':
    main()