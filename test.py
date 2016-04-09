#!/usr/bin/env python
# coding=utf-8
# 这个文件是试验语法或者试验效果的临时文件,杂乱且无规律,只为效率,请勿吐槽.

# a = {'a': "a"}
# print a["a"]
# print a["b"]

# import ctypes
# a = "hello world"
# print ctypes.cast(id(a), ctypes.py_object).value


# def change(a):
# #     print 'id a ', id(a)
    # a = 10
#     print ctypes.cast(id(a), ctypes.py_object).value
#     print n,'haha'
#     print 'id a =10 ', id(a)
#     return id(a)
#
#
# def changeb(a):
#     print 'id a[] ', id(a)
#     a[0] = 10
#     print 'id a[0] =10 ', id(a)
#
# n = 2
#
# m = [2]
# print id(m)
#
# print 'id n', id(n), 'id m', id(m)
#
#
# c = change(n)
# print n
# print ctypes.cast(c, ctypes.py_object).value
#
# changeb(m)
#
#
# print m[0]
# print m
#
# a = 'hahah'
# print a
# a = 2333

# a = 2
# b = 2
# print id(a), id(b)


# print a
# def tt(count):
#     a, b = 0, 1
#     while a < count:
#         yield a
#         a, b = b, a+b
#
# for i in tt(9):
#     print i

# def  seet(a):
#     b = set(a)
#     return list(b)
#
# a = [1,2,3,4,4,5,5]
# print seet(a)

# class from_obj(object):
#     def __init__(self, to_obj):
#         self.to_obj = to_obj
#
# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print(id(b))
# print globals()

# import gc
# print(gc.get_threshold())
#
# x = [1, 2, 3]
# y = [x, dict(key1=x)]
# z = [y, (x, y)]
#
# import objgraph
# objgraph.show_refs([z], filename='ref_topo.png')
# lista = [1,2,3,4,5,-1,-3]
# listb = [i for i in lista if -i in lista]
# print listb

# a = 257
# b = 257
# print  id(a) == id(b)

# lista = [3]*3000
# c =(lista)
# print id(c)
# print ctypes.cast(id(c), ctypes.py_object).value
#
# def get_no_of_instances(cls_obj):
#     return cls_obj.no_inst
#
# class Kls(object):
#     no_inst = 0
#
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
#         print no_inst
#
# ik1 = Kls()
# ik2 = Kls()
#
# print(get_no_of_instances(ik2))

# a = (1,2,3)
# print "%s" % (a,)
# a = []
# a = None
# print len(a)
# if not a:
#     print 'hahah'

# a ={'a':1,'b':2}
# a.
# a = [1,2,3,4,5,6]
# print id(a)
# b= a[:] = [i for i in a if i%2==0 ]
# print a,b,id(a),id(b)
# a = [1,2,3]
# a[1:1] = [7]
# print a
#
# a.__
# a = [1,2,3,4,5]
# def change(t):
#     t[:] = t[::2]
#
#
# change(a)
# print a

# def make_counter():
#     i = 0
#     def counter(): # counter() is a closure
#         # nonlocal i python 3 的关键字
#         i += 1
#         return i
#     return counter
#
# c1 = make_counter()
# c2 = make_counter()
#
# print (c1(), c1(), c2(), c2())
# # -> 1 2 1 2

# import fileinput
# for line in fileinput.input():
#     print line


# import sys
# for line in sys.stdin:
#     print line

# def inina(retry_count=10):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             while retry_count:
#                 try:
#                     df = func(*args, **kwargs)
#                     retry_count -= 1
#                     if not df.empty:
#                         break
#                 except Exception as e:
#                     print (e)
#             return df
#         return wrapper
#     return decorate
#
#
# @inina
# def test(a, b):
#     print a+b
#     a, b = b, a+b
#
#
# test(1, 2)

# def fun1(a):
#     def fun2():
#         print a
#     return fun2()
#
# fun1('3')


# def inc():
#     x = [0]
#     # x = 0
#     def inner():
#         x[0] += 1
#         # x += 1
#         print(x[0])
#         # print x
#     return inner
# inc1 = inc()
# print inc1.__defaults__
# inc2 = inc()
#
# inc1()
# inc1()
# inc1()
# inc2()

# n 个任务
# m 个处理器
# ti 函数
# 最短时间?
# m 个小写 M个大写 小写拍在前 大写排在后 O(N)时间复杂度

# # def charq(list):
# a = [1,2,3]
# a[1:1] = [7]
# print a

# def decorator(name):
#     print "在这里使用装饰器的name参数：", name
#     def wrapper(func):
#         print "在这里也可用装饰器的name参数：", name
#         def _wrapper(*args, **kwargs):
#             print "这里还可使用装饰器的name参数：", name
#             ret = func(*args, **kwargs)    # 这里进行原函数的计算
#             return ret*2
#         return _wrapper                    # 返回可调用对象，_wrapper可以接受原函数的参数
#     return wrapper                         # 返回真正的装饰器，接受原函数作为第一个参数
#
# @decorator(u'haha')
# def wait_for_deco(x, y):
#     return x + y
#
# # wait_for_deco = decorator(u'haha')(x, y)


# import collections
# tree = lambda: collections.defaultdict(tree)
# some_dict = tree()
# some_dict['colours']['favourite'] = "yellow"
# # print some_dict
#
# import json
# print(json.dumps(some_dict))

# from collections import defaultdict
# some_dict = defaultdict(dict)
# some_dict['colours']
# some_dict['colours']['favourite'] = "yellow"
#
# for i in some_dict:
#     print i,some_dict[i]

# user = {'name': "Trey", 'website': "http://treyhunner.com"}
#
# defaults = {'name': "Anonymous User", 'page_name': "Profile Page"}
#
# # context = {**defaults, **user}  # 解包只能在py3 里用
#
#
# # from collections import ChainMap
# # context = dict(ChainMap(user, defaults))  # Py3 加入的
#
# # context = {}
# # context.update(defaults)
# # context.update(user)
#
# context = defaults.copy()
# context.update(user)
# print user, '\n', defaults, '\n', context
