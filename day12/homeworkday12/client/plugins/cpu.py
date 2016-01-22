#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import commands

def monitory():
    shell_command = 'sar 1 3|grep "^Average:"'
    status,result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status':status}
    else:
        user,nice,system,iowait,steal,idle = result.split()[2:] #取出命令结果除了命令返回的状态
        value_dic = {
            'user':user,
            'nice':nice,
            'system':system,
            'iowait':iowait,
            'steal':steal,
            'idle':idle,
            'status':status
        }