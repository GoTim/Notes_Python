#!/usr/bin/env python 
#-*- coding:utf-8 -*_-

import getpass

count = 0

for i in range(3):
    input_user = raw_input("�������û���: ")
    input_pwd = getpass.getpass("����������: ")
    check_lock = file('lockuser','r') #�򿪱����û��ļ����鿴�û��Ƿ���
    lock_user = check_lock.readlines() #ÿ�ж�ȡ
    user_login_flag = False
    
    for line in lock_user:
        line = line.strip('\n')  #ȡ���س���
        if input_user == line:       #����û��Ƿ���
            print "%s �û��Ǳ������ģ�����ϵ����Ա������"  % input_user
            user_login_flag = True
            break        
    if user_login_flag:
        user_login_flag = True
        break
    
    user_list = file('userlist','r')
    user_line = user_list.readlines()   #ÿ�ж�ȡ
    
    for userline in user_line:
        value_name = userline.strip()
        user_list = value_name.split(';')
        user_name = user_list[0]    #��ȡ�û���
        user_pwd = user_list[1]     #��ȡ����
        
        if input_user == "guest":
            print "��ӭ%s"  % input_user
            user_login_flag = True
            break
        elif input_user == user_name and input_pwd == user_pwd:  #�ж��ǿ����û�����������ȷ����¼
            print "��ӭ%s ��¼ϵͳ" % input_user
            user_login_flag = True
            break
        elif input_user == user_name and input_pwd != user_pwd:  #�ж��ǿ����û������������󣡳���3�Σ�����
            print "������������������������룺"
            while True:
                count += 1
                input_pwd = getpass.getpass("����������: ")
                user_login_flag = False
                
                if  input_pwd == user_pwd:
                    print "��ӭ%s ��¼ϵͳ" % input_user
                    user_login_flag = True
                    break
                else:
                    print "������������������������룺"
                if count == 2:  #�����������3�����������
                    tolock = open('lockuser','a')
                    tolock.write(input_user)   #д��ֻ�����ļ�����������ʱ����ȡ
                    tolock.write("\n")                          
                    tolock.close
                    print "%s �û���ϵ�������3�������ѱ�����������ϵ����Ա����" % input_user
                    user_login_flag = True
                    break
            if user_login_flag:
                user_login_flag = True
                break

    if user_login_flag:
        break
    else:
        print "�������%s�û�����Ч������������" % input_user
else:
    print "�����������3���û���������ϵͳ���˳���"