import sys
import os
import datetime
import time
import config_file as cfg_file

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def load_pocs_from_directory(poc_dir):
    poc_list = []
    sys.path.append(poc_dir)

    for file in os.listdir(poc_dir):
        if file.endswith('.py') and not file.startswith('__init__'):
            module_name = file[:-3]
            module = __import__(module_name)
            poc_list.append(module)
    return poc_list

def run_pocs(pocs, target_url):
    res = [['[INFO]: 开始扫描 {}'.format(target_url)]]
    for poc in pocs:
        if hasattr(poc, 'main'):
            res.append(poc.main(target_url))
        elif hasattr(poc, 'check'):
            res.append(poc.check(target_url))
    res.append(['[INFO]: 结束扫描 {}'.format(target_url)])
    return res

def Deal(target_url): 
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    print(now_time() + " [INFO]正在检测:{}".format(target_url))

def execute_pocs(target_url, poc_dir):
    Deal(target_url)
    pocs = load_pocs_from_directory(poc_dir)
    return run_pocs(pocs, target_url)

def yyoa(target_url):
    poc_dir = 'main/yonyou'
    return execute_pocs(target_url, poc_dir)

def zyoa(target_url):
    poc_dir = 'main/seeyou'
    return execute_pocs(target_url, poc_dir)

def tdoa(target_url):
    poc_dir = 'main/Anywhere'
    return execute_pocs(target_url, poc_dir)
    
def whoa(target_url):
    poc_dir = 'main/ezoffice'
    return execute_pocs(target_url, poc_dir)

def lloa(target_url):
    poc_dir = 'main/Landray'
    return execute_pocs(target_url, poc_dir)

def fwoa(target_url):
    poc_dir = 'main/weaver'
    return execute_pocs(target_url, poc_dir)
