import sys
import os
import rich         #富文本输出库
import time
import cmd2 as cmd  #交互式命令库
from rich.console import Console 
import config_file as cfg_file
from os import 3, read, system, name #用于返回当前操作系统中目录分隔符之外的备选分隔符；用于从文件中读取指定数量的字节；用于在操作系统中执行命令；返回操作系统的名称；
import main
import main.deal
import main.mode

console = Console()
def loading():#加载进入界面
    for i in range(0,105):
        time.sleep(0.005)
        print('-',end = "", file=sys.stdout, flush=True)
def index():
    if name=='nt':      #判断是否为Windows系统
        _ = system('cls')
        print('''
                -----------OA漏扫工具-----------
        使用时请先查看使用说明
                                   OA参数：
                                            zyscan:致远OA漏洞POC
                                            tdscan:通达OA漏洞POC
                                            yyscan:用友OA漏洞POC
                                            whscan:万户OA漏洞POC
                                            llscan:蓝凌OA漏洞POC
                                            fwscan:泛微OA漏洞POC
        _________________________________________________________________________________________________
        
        show:帮助和说明  clear:清屏                                          
        ''')  
    else:
        _ = system('clear')
        print('''
           OA
          使用时请先查看使用说明
                                   命令帮助：
                                            zyscan:致远OA漏洞POC
                                            tdscan:通达OA漏洞POC
                                            yyscan:用友OA漏洞POC
                                            whscan:万户OA漏洞POC
                                            llscan:蓝凌OA漏洞POC
                                            fwscan:泛微OA漏洞POC
        ________________________________________________________________________________________________
        
        show:帮助和说明 ctrl+z:返回 clear:清屏                                          
        ''')
        
class hacktools(cmd.Cmd):
    prompt = time.strftime('\r\n\033[1;31mAction >>\033[32m')
     
    def do_install(self, line):
        main.main.install()
    def do_zyscan(self, line):
        #致远OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input('\033[1;31mzyscan >>\033[32m')
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.zypoc(xz, target_url)        
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.zypoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return
            
            
    def do_tdscan(self, line):
        #通达OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mtdscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.tdpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.tdpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return
            
            
    def do_yyscan(self, line):
        #用友OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31myyscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.yypoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.yypoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_whscan(self, line):
        #万户OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mwhscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.whpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.whpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_llscan(self, line):
        #蓝凌OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mllscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.llpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.llpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return


    def do_fwscan(self, line):
        #泛微OA漏洞POC
        print('''\033[33m
        action:单url扫描
        actions:文件批量扫描
        ''')
        xz = input("\033[1;31mfwscan >>\033[32m")
        if xz == 'action':
            target_url = input("\033[1;31m请输入扫描Url：\033[32m")
            main.mode.fwpoc(xz, target_url)
        elif xz == 'actions':
            target_url = input("\033[1;31m请输入扫描文件地址：\033[32m")
            main.mode.fwpoc(xz, target_url)
        elif xz =='exit':
            return
        else:
            loading()
            console.print('''\r\n
输入的参数有误,返回上一层''', style='bold red')
            return
        
        
    def do_exit(self, line):
        try:
            sys.exit()
            os.system('cls')
            client = Client()
            client.cmdloop()
        except:
            exit()
            

    def do_clear(self, line):
        '''清屏'''
        _ = system('cls')
        index()
    
    def do_show(self, line):
        print('''------法律免责声明:未经事先双方同意攻击目标是非法的。------''')
        list=['tdscan:通达OA漏洞POC','whscan:万户OA漏洞POC','llscan:蓝凌OA漏洞POC','zyscan:致远OA漏洞POC','fwscan:泛微OA漏洞POC','yyscan:用友OA漏洞POC']
        print('''
使用说明:输入相对应的OA系统命令进入对应的模块
-----------------------------------------------------------------------------------------------
已收录的OA:
        ''')
        for i in list:
            print('''\033[33m       {}\033[37m'''.format(i))
            time.sleep(0.015)
            
        print(''' 如果遇到问题请联系 ''')

        
if __name__ == '__main__':
    loading()
    index()
    hacktools().cmdloop()
