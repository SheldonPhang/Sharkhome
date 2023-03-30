# -*- coding: utf-8 -*-
import main.main
import main.deal

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
    res=select(user,target,name)
    return res

def select(user, target, name):
    if user == 'url':
        res = []
        res = main.main.urlDeal(target, name)
        return res
    if user == 'urls':
        res = []
        res = main.main.fileDeal(target, name)
        return res
