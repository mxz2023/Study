# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/26 23:54
@Auth ： 浮生半日闲
@File ： day1.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
from functools import cmp_to_key

# 列表
# 列表中可以存储任意类型的数据，且可以不相同
alist = [1, 'bobo', 12.34, 1, "bobo", "bobo"]

print(alist[-1])  # 'bobo'
print(alist[2])  # 12.34

try:
    # 使用索引和切片的时候，不可以访问超出索引范围的元素
    print(alist[6])
except IndexError as e:
    print(e)

# 切片的语法是： list[start:end:step],注意，区间是左闭右开的.
print(alist[0:2])  # [1, 'bobo']
print(alist[0:3])  # [1, 'bobo', 12.34]
print(alist[:-1])  # [1, 'bobo', 12.34, 1, 'bobo']
print(alist[::-1])  # ['bobo', 'bobo', 1, 12.34, 'bobo', 1]

alist.append('bobo')
alist.append(1)

print(alist.count(1))  # 3
print(alist.count('bobo'))  # 4

items = [1, 2, 3, 4]

# 在末尾追加一个数组
alist.extend(items)
print(alist)  # [1, 'bobo', 12.34, 1, 'bobo', 'bobo', 'bobo', 1, 1, 2, 3, 4]

# 第一次出现的索引
print(alist.index('bobo'))  # 1

# 移除列表一个元素，默认最后一个，返回元素值
print(alist.pop(-2))  # 3

alist.remove('bobo')
print(alist)  # [1, 12.34, 1, 'bobo', 'bobo', 'bobo', 1, 1, 2, 4]

alist.reverse()
print(alist)  # [4, 2, 1, 1, 'bobo', 'bobo', 'bobo', 1, 12.34, 1]

# 排序
items = [1, 2, 54, 6, 78, 89]
items.sort()
print(items)  # [1, 2, 6, 54, 78, 89]

alist.sort(key=str)
print(alist)  # [1, 1, 1, 12.34, 2, 4, 78, 'bobo', 'bobo', 'bobo']

# 插入元素
alist.insert(1, 'abc')
print(alist)  # [1, 'abc', 1, 1, 12.34, 2, 4, 78, 'bobo', 'bobo', 'bobo']


# 自定义排序规则
def cmp(a, b):
    if type(a) is str:
        if type(b) is str:
            return 0 if a > b else -1
        else:
            return -1
    else:
        if type(b) is int:
            return 0 if a > b else -1
        else:
            return 0


items = [1, 10, 9, 'abc', 'ced', 'ace', 100, 78, -1]

items.sort(key=str)
print(items)  # [-1, 1, 9, 10, 78, 100, 'abc', 'ace', 'ced']

items.sort(key=cmp_to_key(cmp))
print(items)  # ['abc', 'ace', 'ced', -1, 1, 9, 10, 78, 100]

# 列表转字符串，数字元素需要转为字符串
ret = '-'.join([str(x) for x in items])
print(ret)  # abc-ace-ced--1-1-9-10-78-100

# 以上为列表 --------------------------------------------------------

# 字典
# 字典中无法存储重复的键值对
dict_1 = {'name': 'bobo', 'age': 18, 'score': 100, 'age': 18}
print(dict_1)  # {'name': 'bobo', 'age': 18, 'score': 100}

# 注意：不要在字段中存储相同的key，value可以相同
dict_2 = {'name': 'bobo', 'age': 18, 'age': 20}
print(dict_2)  # {'name': 'bobo', 'age': 20}

d = {'name': 'bobo', 'age': 20, "scores": [100, 120, 99]}
# 根据key访问对应的value值
print(d['name'], d['scores'])  # 依次访问name和scores对应的value值
print(d.get('name'))  # 通过get使用对应的key访问对应的value值

# 注意：使用[]访问不存在的key对应的value值程序会报错
try:
    print(d['adress'])
except KeyError as e:
    print(e)

# 注意：使用get访问不存在的key程序不会报错，但是会返回None这个空值
print(d.get('address'))

d = {'name': 'bobo', 'age': 20, "scores": [100, 120, 99]}
d['name'] = 'jay'  # 给存在的key修改对应的value值
d['address'] = 'Beijing'  # 给一个不存在的key赋值表示新增键值对
del d['age']  # 删除age键值对
print(d)

d = {'name': 'bobo', 'age': 20, "scores": [100, 120, 99]}
print('name' in d)  # 查看name是否存在于d字典的keys中
print(d.keys())  # 返回字典中所有的key
print(d.values())  # 返回字典中所有的value
print(d.items())  # 返回字典中所有的键值对

# 遍历字典
for key in d.keys():
    print(key, d[key])


# 以上为列表 --------------------------------------------------------

# 函数
# 返回多个值
def func():
    a = 1
    b = ['bobo', '100']
    c = 'jay'

    return a, b, c


ret = func()
print(ret)  # (1, ['bobo', '100'], 'jay')


# 不写return，默认返回None
def cal():
    print('我是函数')


ret = cal()
print(ret)  # None


# 返回一个函数（适当理解）
def outer():
    print('正在执行outer函数')

    def inner():
        print('正在执行inner函数')

    print('outer函数执行结束')

    return inner


ret = outer()  # outer() == inner == ret
ret()  # inner()


# 返回一个函数调用（适当理解）
def outer():
    print('正在执行outer函数')

    def inner():
        print('正在执行inner函数')
        return 123

    print('outer函数执行结束')

    return inner()  # 123 == inner()


ret = outer()  # inner() == 123 == ret
print(ret)


# 通常我们在调用函数时，位置参数都是按顺序先后传入。但是，如果在位置参数传递时，给实参指定位置参数的参数名，那么位置参数也可以不按顺序调用。
def student(name, sex, age):
    return name, sex, age


ret = student('bobo', 'male', 20)
print(ret)  # ('bobo', 'male', 20)
ret = student(sex='male', name='bobo', age=20)
print(ret)  # ('bobo', 'male', 20)


def func(*args):  # 动态参数
    print(args)


func(1, 2, 'three', [6, 7])


def func(*args):
    print(args)


func(*[1, 2, 3, 4, 5])


def func(**kwargs):
    print(kwargs)


func(k1=1, k2=2, k3='bobo')

# 以上为列表 --------------------------------------------------------
