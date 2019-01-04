#!/usr/bin/env python
# -*-coding:utf-8 -*-

import random

dic={}
lis = ['KeLan','Monkey','Dexter','Superman','Iron Man','Robin']

def redpacket(cash,person,index):
    if cash>0 and person !=1:
        if (cash-(1*person)) > 20:
            n = round(random.uniform(1,20),2)
        else:
            n = round((random.uniform(1,cash-(1*person))),2)
        dic[lis[index]] = n
        print str(n).ljust(4,"0")
        # person-=1
        # cash-=n
        # index+=1
        redpacket(cash-n,person-1,index+1)
    else:
        dic[lis[index]]=round(cash,2)
        print str(cash).ljust(4,"0")


if __name__ == '__main__':
    redpacket(100,len(lis),0)
    print dic
    print "手气最佳:",max(dic.items(),key=lambda x:x[1])