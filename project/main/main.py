import os
import sys
import datetime
import multiprocessing
import socket, socks
import config_file as cfg_file
'''import main.deal'''
import main.deal


def fileDeal(target, name):
    file_object = open(target, 'r')
    try:
        lines = file_object.readlines()
        pool = multiprocessing.Pool()
        # 使用 map 方法代替 apply 方法````````````````````
        results = pool.map(name, [url.strip('\n') for url in lines])
        pool.close()
        pool.join()
        # 将所有的结果展开成一个平坦的列表
        res = [item for sublist in results for item in sublist]
        return res
    except KeyboardInterrupt:
        print('\nCTRL+C 退出')
    finally:
        file_object.close()

def urlDeal(target,name):
    try:
        res = name(target)
#        print(res[0],res[2],res[3],res[4],res[5])
        return res
    except KeyboardInterrupt:
        print('\nCTRL+C 退出')

'''if __name__== "__main__" :
    main()'''
        



    

    