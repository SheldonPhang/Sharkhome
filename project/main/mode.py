# -*- coding: utf-8 -*-
import main.main
import main.deal
from main.deal import res_queue



def get_results():
    results = []
    while not res_queue.empty():
        results.append(res_queue.get())
    return results

def yypoc(user, target):
    name=main.deal.yyoa
    res=select(user,target,name)
    return res
    
def zypoc(user, target):
    name=main.deal.zyoa
    res=select(user,target,name)
    return res

def tdpoc(user, target):
    name=main.deal.tdoa
    res=select(user,target,name)
    return res
    
def whpoc(user, target):
    name=main.deal.whoa
    res=select(user,target,name)
    return res
    
def llpoc(user, target):
    name=main.deal.lloa
    res=select(user,target,name)
    return res
        
def fwpoc(user, target):
    name=main.deal.fwoa
    res=select(user,target,name)
    return res

def addpoc(user, target):
    name=main.deal.useraddoa
    res = select(user, target, name)
    return res

def select(user, target, name):
    if user == 'url':
        main.main.urlDeal(target, name)
    if user == 'urls':
        main.main.fileDeal(target, name)
    res = get_results()
    return res
