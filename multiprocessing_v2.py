# -*- coding: utf-8 -*-
"""
多进程测试
"""

import requests
from multiprocessing import Pool
from time import time


URLS = [
       'https://www.baidu.com',
       'https://download.csdn.net/',
       'https://mp.weixin.qq.com/',
       'http://www.wps.cn/product/beta/',
       'https://www.etymonline.com/',
       'http://docs.python-requests.org/en/master/',
       'https://www.zhihu.com',
       'http://bbs.pinggu.org/',
       'http://www.tianya.cn/',
       'https://coderprog.com/',
       'https://zooqle.com/',    
       ]

HEADER = {'User-Agent': 'Mozilla/5.0'}
#自定义全局进程数
PROCESS_POOL_SIZE = 10


def worker(url):
    print('{:50}'.format(url), end='')
    try:
        r = requests.get(url, headers=HEADER)
        r.raise_for_status
        print('\tSuccess!')
    except Exception as e:
        print('\tFailed!')

def main():     
    with Pool(10) as pool:
        pool.map(worker, URLS)    
 
#测试脚本
if __name__ == '__main__':    
    start = time()
    main()
    end = time()
    print('进程数：{}个\n总耗时：{:.2f} 秒'.format(PROCESS_POOL_SIZE,end-start))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    