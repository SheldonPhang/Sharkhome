import os
import sys
import datetime
import multiprocessing
import socket, socks
import main.deal


def fileDeal(target, name):
    file_object = open(target, 'r')
    try:
        lines = file_object.readlines()
        pool = multiprocessing.Pool()
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
        return res
    except KeyboardInterrupt:
        print('\nCTRL+C 退出')
