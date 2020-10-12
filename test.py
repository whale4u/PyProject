# def outer(func):
#     def inner(username):
#         print("认证成功！")
#         result = func(username)
#         print("日志添加成功")
#         return result
#     return inner
#
# @outer
# def f1(name):
#     print("%s 正在连接业务部门1数据接口......"%name)
#
# # 调用方法
# f1("jack")


list1 = [3, 43, 2, 4, 2, 3]
dict_cnt = {}  # dict_cnt=dict()
for item in list1:
    if item in dict_cnt:  # 直接判断key在不在字典中
        dict_cnt[item] += 1
    else:
        dict_cnt[item] = 1

print(dict_cnt)