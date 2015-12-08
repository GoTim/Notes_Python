#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
该计算器思路：
    1、递归寻找表达式中只含有 数字和运算符的表达式，并计算结果
    2、由于整数计算会忽略小数，所有的数字都认为是浮点型操作，以此来保留小数
使用技术：
    1、正则表达式
    2、递归
"""
import re
def compute_mul_div(arg):
    """ 操作乘除
    :param expression:方程式
    :return:计算结果
    """
    val = arg[0]  #获取整个方程式
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)  #获取乘除方程式
    if not mch: #判断是否知道乘除的方程式，如果没有直接return
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val).group() #获取乘除的算式
 
    if len(content.split('*'))>1: #判断用*分割后的列表元素个数是否大于1，如果大于1说明获取的是乘法算式
        n1, n2 = content.split('*')
        value = float(n1) * float(n2) #用浮点进行计算
    else:
        n1, n2 = content.split('/') #除法算是
        value = float(n1) / float(n2)   #用浮点进行计算
 
    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1) #获取第一个乘除的算式，并用这个算式分割
    new_str = "%s%s%s" % (before,value,after) #把计算结果进行拼接，获得新的方程式
    arg[0] = new_str #写入至列表中
    compute_mul_div(arg)  #递归计算
 
 
def compute_add_sub(arg):
    """ 操作加减
    :param expression:表达式
    :return:计算结果
    """
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__("--"):
            '''
            __contains__ 如果找到我们们定义的item就会返回True
            '''
            arg[0] = arg[0].replace('+-','-') #替换运算符
            arg[0] = arg[0].replace('++','+') #替换运算符
            arg[0] = arg[0].replace('-+','-') #替换运算符
            arg[0] = arg[0].replace('--','+') #替换运算符
        else:
            break
 
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-','&')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('&','+')
        arg[0] = arg[0][1:]
    val = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    if len(content.split('+'))>1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)
 
    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_add_sub(arg)
 
 
def compute(expression):
    """ 操作加减乘除
    :param expression:表达式
    :return:计算结果
    """
    inp = [expression,0]
 
    # 处理表达式中的乘除
    compute_mul_div(inp)
 
    # 处理
    compute_add_sub(inp)
    if divmod(inp[1],2)[1] == 1:
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])
    return result
 
 
def exec_bracket(expression):
    """ 递归处理括号，并计算
    :param expression: 表达式
    :return:最终计算结果
    """
    # 如果表达式中已经没有括号，则直接调用负责计算的函数，将表达式结果返回
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
        final = compute(expression)
        return final
    # 获取 第一个 只含有 数字/小数 和 操作符 的括号
    # 如：
    #    ['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    #    找出：(-40.0/5)
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression).group()
 
    # 分割表达式，即：
    # 将['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    # 分割更三部分：['1-2*((60-30+(    (-40.0/5)      *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)
 
    print 'before：',expression
    content = content[1:len(content)-1]
 
    # 计算，提取的表示 (-40.0/5)，并活的结果，即：-40.0/5=-8.0
    ret = compute(content)
 
    print '%s=%s' %( content, ret)
 
    # 将执行结果拼接，['1-2*((60-30+(      -8.0     *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
    expression = "%s%s%s" %(before, ret, after)
    print 'after：',expression
    print "="*10,'上一次计算结束',"="*10
 
    # 循环继续下次括号处理操作，本次携带者的是已被处理后的表达式，即：
    # ['1-2*((60-30+   -8.0  *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
 
    # 如此周而复始的操作，直到表达式中不再含有括号
    return exec_bracket(expression)
 
 
 
# 使用 __name__ 的目的：
#   只有执行 python index.py 时，以下代码才执行
#   如果其他人导入该模块，以下代码不执行
if __name__ == "__main__":
    #print '*'*20,"请计算表达式：", "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )" ,'*'*20
    inpp = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
    #inpp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    #inpp = "1-5*980.0"
    inpp = re.sub('\s*','',inpp)
    # 表达式保存在列表中
    result = exec_bracket(inpp)
    print result