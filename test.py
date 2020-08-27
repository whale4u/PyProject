def outer(func):
    def inner(username):
        print("认证成功！")
        result = func(username)
        print("日志添加成功")
        return result
    return inner

@outer
def f1(name):
    print("%s 正在连接业务部门1数据接口......"%name)

# 调用方法
f1("jack")