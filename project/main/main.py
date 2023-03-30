import os
import sys
import datetime
import multiprocessing
import socket, socks
import config_file as cfg_file
import main.deal
from concurrent.futures import ThreadPoolExecutor

def fileDeal(target, name):
    file_object = open(target, 'r')
    results = []
    try:
        lines = file_object.readlines()
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(name, [url.strip('\n') for url in lines]))
          #   results = list(executor.map(lambda x: name(x, target), [url.strip('\n') for url in lines]))

        return results
    except KeyboardInterrupt:
        print('\nCTRL+C 退出')
    finally:
        file_object.close()

def urlDeal(target, name):
    try:
        return name(target)
    except KeyboardInterrupt:
        print('\nCTRL+C 退出')


