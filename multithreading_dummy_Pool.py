# -*- coding: utf-8 -*-
"""
多线程测试版本二

::使用多进程模块中的dummy.pool模块。此模块提供了与多进程池同样的接口，
但用于多线程。无需考虑手动配置线程池，也无需配置队列以供线程之间额通信，
模块内部已经实现了相应的功能。
::程序结构无需作任何改变，仅需将dummy模块导入即可。非常方便。在一些特殊
的场合可以根据输入或者配置文件切换使用进程或者线程方式。
"""

import requests
from multiprocessing.dummy import Pool
from time import time


URLS = ['https://www.baidu.com',
        'https://download.csdn.net/',
        'https://mp.weixin.qq.com/',
        'http://www.wps.cn/product/beta/',
        'https://www.etymonline.com/',
        'http://docs.python-requests.org/en/master/',
        'https://www.zhihu.com',
        'http://bbs.pinggu.org/',
        'http://www.tianya.cn/',
        'https://coderprog.com/',
        'https://zooqle.com/']


HEADER = {'User-Agent': 'Mozilla/5.0'}
#自定义全局进程数
POOL_SIZE = 10

def worker(url):
    print('{:50}'.format(url), end='')
    try:
        r = requests.get(url, headers=HEADER)
        r.raise_for_status
        print('\tSuccess!')
    except Exception as e:
        print('\tFailed!')
              

def main():     
    with Pool(POOL_SIZE) as pool:
        pool.map(worker, URLS)   
              
 
#测试脚本
if __name__ == '__main__':    
    start = time()
    main()
    end = time()
    print('线程数：{}个\n总耗时：{:.2f} 秒'.format(POOL_SIZE,end-start))

