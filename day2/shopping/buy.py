#!/usr/bin/env python
#-*- coding:utf-8 -*-

surplus_money = file('surplus.txt','r') #��ȡʣ��Ǯ��
for list_money in surplus_money:
    list_money = int(list_money)
    print "\033[34;1m���ϴ�ʣ�ࣺ\033[0m \033[32;1m%d\033[0m \033[34;1m\033[0m" % list_money
    
ask_recharge = raw_input("\033[32;1m���Ƿ����ֵһЩ����أ�������yes/no:\033[0m ") #ѯ���û��Ƿ���Ҫ��ֵǮ
if ask_recharge == "yes" or ask_recharge == "YES":
    salary_money = int(raw_input("\033[32;1m��������Ҫ��ֵ�Ľ��:\033[0m"))
    salary = list_money + salary_money
    print "\033[34;1m�ǳ���л���ĳ�ֵ�����ڵĽ���ǣ�\033[0m \033[31;1m%s\033[0m  \033[34;1 ,ϣ�����������\033[0m" % salary
else:
    salary = list_money   

print "\033[32;1m��ӭ���ٱ��̳��������Ǳ��̳�����������Ʒ��������������Ʒ�Ź���:\033[0m"
'''
salary = input("please input your budget:")
'''

product_list = [
    ('Iphon',5800),
    ('Bike',800),
    ('Book',45),
    ('Coffee',35),
    ('iphon touch',1590),
    ('MX4',1999)
]
shoping_list = []

while True:
    index = 1  #��������ֵ��1��ʼ
    for item in product_list:
        print "\033[32;1m%s: %s\t%s\033[0m" %(index,item[0],item[1])
        index += 1
    
    user_choice = int(raw_input("\033[33;1m��ܰ��ʾ:����0�Ƴ�����\033[0m|\033[34;1m�������кŹ�����Ʒ����������Ҫ����ʲô��Ʒ��\033[0m ").strip()) #.strip()�ѿո�ȡ��
    if user_choice == 0:
        ask_exit = raw_input("\033[33;1mΪ�˷�ֹ�������������˳�������yes/YES,����������������ع����б�:\033[0m")
        if ask_exit == "yes" or ask_exit == "YES":
            print "\033[34;1m�����������εĹ����嵥��\033[0m"
            for buy_list in shoping_list:
                print "\033[34;1m%s \033[0m" % buy_list[0]  #��ӡshoping_list �û������б�
            sum_money = 0
            for buy_money in shoping_list:
                sum_money += buy_money[1]
            print "\033[32;1m�������ܹ����ѽ��Ϊ��%d \033[0m" % sum_money #��ӡ�ܹ������˶���Ǯ
            print "\033[32;1m������ʣ����Ϊ��%s ʣ����ᱣ�浽����ϵͳ���´ι���ʱ����ֱ��ʹ�ã�\033[0m" % salary  #��ӡ����ʣ���
            last_money = str(salary)
            buy_surplus = file('surplus.txt','w+')
            buy_surplus.write(last_money)
            buy_surplus.write('\n')
            buy_surplus.close
            break
        else:
            continue
    user_choice -= 1 #������Ϊ�Ǵ�1��ʼ����������Ҫ-1 Ҫ��Ȼ��������������ʱ��������⣡
    if user_choice >= index:
        print "Please enter the correct serial number "
        continue
    item_price = product_list[user_choice][1]
    if salary >= item_price:   #�ж����еĽ���Ƿ������Ʒ�۸�
        salary -= item_price  #������ڹ����ȥ��Ʒ�۸�
        shoping_list.append(product_list[user_choice])
        print "\033[34;1m��Ʒ %s �ѹ��򲢼��빺�ﳵ\033[0m" % product_list[user_choice][0]  #��ӡ���ֵ�����б�
        print "\033[33;1m������ʣ����Ϊ�� %s \033[0m" %salary #���ӡ��ʣ�����
    else:
        print "\033[31;1m������˼��ʣ����ܹ��� %s ��������ʣ��%s,�����鿴���̳�������Ʒ!\033[0m " % (product_list[user_choice][0],salary) #ʣ��Ǯ������ʾ��
      