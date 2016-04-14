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

# compile('hahha')

# from decimal import *

# a = [1,2,3]
# print id(a)
# a.insert(0,8)
# # a[0:0] = [8]
# print a,id(a)
#
# b = 2
#
# print type(a),type(b)
# print type(a) == type(b)
# print type(a) is type(b)
#
# print dir( )
#
# a = 10
# b = 10
# c = 1000
# d = 1000
# e = 10.0
# f = 10.0
# print a is b
# print c is d
# print e is f

# print dir().getfile()

# for i in  range(2):
#     print i
#
# for i in range(4,6):
#     print i

# class Person:
#     def __init__(self):
#         pass
#
#     def getAge(self):
#         print __name__
#
# p = Person()
# p.getAge()

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
#
# if 'amir' in names1:
#     print 1
# else:
#     print 2

# numbers = [1, 2, 3, 4]
#
# numbers.append([5,6,7,8])
#
# print len(numbers)
# print numbers

# kvps = { '1' : 1, '2' : 2 }
# theCopy = kvps.copy()
#
# kvps['1'] = 5
#
# sum = kvps['1'] + theCopy['1']
# print sum

# a = []
# import fileinput
# for index, line in enumerate(fileinput.input()):
#     a[index] = line
# print pow(a[0], a[1])
# print pow(a[0], a[1], a[2])


# a = int(raw_input())
# b = int(raw_input())
# c = int(raw_input())
# print pow(a, b)
# print pow(a, b, c)

# from collections import Counter
#
# data = [0, 2, 4, 5, 2, 2, 2]
#
# for key, value in Counter(data).items():
#     print key, value
#     # if value > (len(data) / 2):
#     #     print(key)
#
# # Out: 2
#
# a = {1:2,2:3,3:4}
# print a.items()
#
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {k: v for d in (x,y) for k, v in d.items()}
# print z
# from pprint import pprint
# mat = [[1,2,3], [4,5,6], [7,8,9]]
# new_mat = [ [row[i] for row in mat] for i in [0,1,2] ] # 嵌套
# pprint(new_mat)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# import random
# def random_pick(seq, probabilities):
#     x = random.uniform(0, 1)
#     cumulative_probability = 0.0
#     for item, item_probability in zip(seq, probabilities):
#             cumulative_probability += item_probability
#             if x < cumulative_probability:
#                 break
#     return item
#
#
# for i in range(15):
#     print random_pick("abc",[0.1,0.3,0.6])

# a = [1,2,3]
# b = list(a)
# print id(a), id(b)  # 140298869519856 140298869576192
# for x, y in zip(a, b):       # 子对象身份相同
#     print(id(x), id(y))
#     # (34189656, 34189656)
#     # (34189632, 34189632)
#     # (34189608, 34189608)

# import copy
# a = [1, 2, 3]
# b = copy.deepcopy(a)
# print id(a), id(b)  # 140298869557512 140298869519856
# for x, y in zip(a, b):       # 子对象身份相同,2333 因为1,2,3是不可变对象
#     print(id(x), id(y))
#     # (34189656, 34189656)
#     # (34189632, 34189632)
#     # (34189608, 34189608)
#
#
# import copy
# a = [[1],[2],[3]]
# b = copy.deepcopy(a)
# print id(a), id(b)  # 139930602280504 139930602280288
# for x, y in zip(a, b):       # 子对象身份不同
#     print(id(x), id(y))
#     # (139930602147208, 139930602280576)
#     # (139930602146056, 139930602280720)
#     # (139930602280216, 139930602280792)
#
# def makeHtmlTag(tag, *args, **kwds):
#     def real_decorator(fn):
#         css_class = " class='{0}'".format(kwds["css_class"]) \
#                                      if "css_class" in kwds else ""
#         def wrapped(*args, **kwds):
#             return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
#         return wrapped
#     return real_decorator
#
# @makeHtmlTag(tag="b", css_class="bold_css")
# @makeHtmlTag(tag="i", css_class="italic_css")
# def hello():
#     return "hello world"
#
# print hello()
# print hello.__name__

# class myDecorator(object):
#
#     def __init__(self, fn):
#         print "inside myDecorator.__init__()"
#         self.fn = fn
#
#     def __call__(self):
#         self.fn()
#         print "inside myDecorator.__call__()"
#
# @myDecorator
# def aFunction():
#     print "inside aFunction()"
#
# print "Finished decorating aFunction()"
#
# aFunction()
#
# # 输出：
# # inside myDecorator.__init__()
# # Finished decorating aFunction()
# # inside aFunction()
# # inside myDecorator.__call__()
#
# from functools import wraps
# def memo(fn):
#     cache = {}
#     # miss = object()
#     miss = 'dd'
#
#     @wraps(fn)
#     def wrapper(*args):
#         # result = cache.get(args)
#         result = cache.get(args, None)
#         if result is None:
#             result = fn(*args)
#             cache[args] = result
#         return result
#
#     return wrapper
#
# @memo
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# import time
# a = time.time()
# print fib(1000)
# print time.time() - a

# import time
# a = time.time()
#
# def test(x):
#     a, b, i = 0, 1, 0
#     while i < x:
#         yield b
#         a, b = b, a+b
#         i += 1
#
# for i in test(10000):
#     pass
# print i
# print time.time() - a
#
# from threading import Thread
# from functools import wraps
#
# def async(func):
#     @wraps(func)
#     def async_func(*args, **kwargs):
#         func_hl = Thread(target = func, args = args, kwargs = kwargs)
#         func_hl.start()
#         return func_hl
#
#     return async_func
#
# if __name__ == '__main__':
#     from time import sleep
#
#     @async
#     def print_somedata():
#         print 'starting print_somedata'
#         sleep(2)
#         print 'print_somedata: 2 sec passed'
#         sleep(2)
#         print 'print_somedata: 2 sec passed'
#         sleep(2)
#         print 'finished print_somedata'
#
#     def main():
#         print_somedata()
#         print 'back in main'
#         print_somedata()
#         print 'back in main'
#
#     main()

# import time
# from functools import wraps
# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         ts = time.time()
#         result = fn(*args, **kwargs)
#         te = time.time()
#         print "function      = {0}".format(fn.__name__)
#         print "    arguments = {0} {1}".format(args, kwargs)
#         print "    return    = {0}".format(result)
#         print "    time      = %.6f sec" % (te-ts)
#         return result
#     return wrapper


# import inspect
# def get_line_number():
#     return inspect.currentframe().f_back.f_back.f_lineno
#
# def logger(loglevel):
#     def log_decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             ts = time.time()
#             result = fn(*args, **kwargs)
#             te = time.time()
#             print "function   = " + fn.__name__,
#             print "    arguments = {0} {1}".format(args, kwargs)
#             print "    return    = {0}".format(result)
#             print "    time      = %.6f sec" % (te-ts)
#             if (loglevel == 'debug'):
#                 print "    called_from_line : " + str(get_line_number())
#             return result
#         return wrapper
#     return log_decorator
#
#
#
# @logger
# def multipy(x, y):
#     return x * y
#
# @logger
# def sum_num(n):
#     s = 0
#     for i in xrange(n+1):
#         s += i
#     return s
#
# print multipy(2, 10)
# # print sum_num(100)
# # print sum_num(10000000)
# from pprint import pprint
# a = ["123", "234", "134"]
# print a
#
# def tuplea(a):
#     return (a[0], a[1])
#
# print sorted(a, key=tuplea)


list_to_be_sorted = [{'name':'Homer', 'age':10, 'sales':100}, {'name':'H1omer', 'age':10, 'sales':200}, {'name':'H2omer', 'age':20, 'sales':300},
                     {'name':'H3omer', 'age':30, 'sales':300}]
newlist = sorted(list_to_be_sorted, key=lambda k: (k['age'], k['sales']))
print newlist
#
# a = {'a':2}
# print a.a
