# -*- coding: utf-8 -*-
import main.main
import main.deal
from main.deal import res_queue

output_func = None

def get_results():
    results = []
    while not res_queue.empty():
        results.append(res_queue.get())
    return results

def select(user, target, name):
    if user == 'url':
        main.main.urlDeal(target, name)
    if user == 'urls':
        main.main.fileDeal(target, name)
    res = get_results()
    return res

def output_result(target, poc):
    output = f'{target} 存在漏洞: {poc.strip(".py")}'
    return output  # 修改为返回结果，而不是直接输出

def yypoc(user, target):
    name = main.deal.yyoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def zypoc(user, target):
    name = main.deal.zyoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def tdpoc(user, target):
    name = main.deal.tdoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def whpoc(user, target):
    name = main.deal.whoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def llpoc(user, target):
    name = main.deal.lloa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def fwpoc(user, target):
    name = main.deal.fwoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)

def addpoc(user, target):
    name = main.deal.useraddoa
    res = select(user, target, name)
    for poc in res:
        output_result(target, poc)
