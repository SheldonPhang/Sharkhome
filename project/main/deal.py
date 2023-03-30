import sys
import os
import datetime
import time
import config_file as cfg_file
import pkgutil
import importlib
from queue import Queue
import main
from main.yonyou import nc_beanshell_rce,nc_upload_rce,nc_erp_sql,nc_u8_test_sql,nc_erp_directory
from main.yonyou import 用友畅捷通T_updata_任意文件上传,nc_U8_getSessionList,fe_oa_directiry, nc_readfile_everything,nc_xbr_rce,用友_U8_f5_sql,用友GRP_u8_upload_data,yongyou_KSOA_imageupload
from main.seeyou import 致远OA_A6_createMysql_数据库敏感信息泄露, 致远OA_A6_DownExcelBeanServlet_用户敏感信息下载, 致远OA_A6_initDataAssess_用户敏感信息泄露, \
    致远OA_A6_setextno_SQL注入Getshell, 致远OA_A6_test_SQL注入Getshell, 致远OA_A8_htmlofficeservlet_RCE, \
    致远OA_getSessionList_Session泄漏, 致远OA_ajax_登录绕过_任意文件上传, 致远OA_webmail_任意文件下载, 致远OA_Session泄露_任意文件上传, 致远OA_Fastjson_反序列化,致远OA_A6_config_jsp敏感信息泄露,致远OA_A8_status_jsp敏感信息泄露

from main.Anywhere import (通达OA_v11_5_swfupload_sql, 通达OA_v11_5_任意用户登录, 通达OA_v11_6_insert_sql, 通达OA_v11_6_report_bi_sql, 通达OA_v11_6_任意文件删除_RCE, 通达OA_v11_7_后台sql注入,通达OA_v11_7_在线用户登录, 通达OA_v11_8_api_任意文件上传, 通达OA_v11_8_getway_远程文件包含, 通达OA_v2014_get_contactlist, 通达OA_v2017_action_upload,通达OA_v2017_任意用户登录,通达OA_v11_8_logincheck,通达OA_v11_8_后台包含xss,通达OA_v11_9_getdata)
from main.ezoffice import (万户OA_download_ftp, 万户OA_download_http, 万户OA_download_old, 万户OA_fileupload_controller,万户OA_office_任意文件上传,万户OA_document_sql,万户OA_smart_upload_文件上传,万户OA_download_servelet)
from main.Landray import (蓝凌OA_任意文件写入, 蓝凌OA_treeXml_远程命令执行, 蓝凌OA_datajson_命令执行, 蓝凌OA_custom_任意文件读取)
from main.weaver import Bsh_RCE,E_Bridge_Arbitrary_File_Read,E_Cology_Database_Leak,E_Cology_V8_Sql,E_Cology_WorkflowServiceXml_RCE
from main.weaver import Weaver_Common_Ctrl_Upload,WorkflowCenterTreeData_Sql,Weaver_V9_uploadOperation,Weaver_oa_infiledonload
from main.weaver import Weaver_e_office_userlogin,E_office_upload,Weaver_e_officeserver_readfile,E_office_group_xml_sql,E_Cology_user_data,E_Cology_LoginsSSo_sql,E_Cology_getData_sql,泛微OA_hrmcareerApply_sql,泛微OA_jquery_filetree,泛微OA_Verify_QuickLogin,泛微OA_mysql_config数据库信息泄漏,泛微OA_signnature_任意文件访问,泛微OA_uploader_OPerate,泛微OA_V10_前台sql,泛微OA_doexcel,泛微OA_ktree_upload,泛微OA_v10_upload,泛微OA_eoffice8_upload,泛微OA_moblie_v6_sql
from main.useradd import testoa

res_queue = Queue()


def import_and_get_pocs(module):
    pocs = []
    for _, name, _ in pkgutil.iter_modules(module.__path__):
        if not name.startswith("_"):
            poc_module = importlib.import_module(module.__name__ + "." + name)
            if hasattr(poc_module, "main") or hasattr(poc_module, "check"):
                pocs.append(poc_module)
    return pocs

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def run_pocs(pocs, target_url):
    res_queue.put('[INFO]: 开始扫描 {}'.format(target_url))
    for poc in pocs:
        if hasattr(poc, 'main'):
            result = poc.main(target_url)
            if result:
                res_queue.put(result)
        elif hasattr(poc, 'check'):
            result = poc.check(target_url)
            if result:
                res_queue.put(result)
    res_queue.put('[INFO]: 结束扫描 {}'.format(target_url))

def Deal(target_url): 
    if target_url[:4] != 'http':
        target_url = 'http://' + target_url
    if target_url[-1] != '/':
        target_url += '/'
    print(now_time() + " [INFO]正在检测:{}".format(target_url))

def execute_pocs(target_url, poc_module):
    Deal(target_url)
    pocs = import_and_get_pocs(poc_module)
    return run_pocs(pocs, target_url)

def yyoa(target_url):
    return execute_pocs(target_url, main.yonyou)

def zyoa(target_url):
    return execute_pocs(target_url, main.seeyou)

def tdoa(target_url):
    return execute_pocs(target_url, main.Anywhere)
    
def whoa(target_url):
    return execute_pocs(target_url, main.ezoffice)

def lloa(target_url):
    return execute_pocs(target_url, main.Landray)

def fwoa(target_url):
    return execute_pocs(target_url, main.weaver)

def useraddoa(target_url):
    return execute_pocs(target_url, main.useradd)
