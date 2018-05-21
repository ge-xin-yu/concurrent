# -*- coding: utf-8 -*-
"""
多线程测试版本一

使用多线程中的Thread模块，此模块需要考虑配置队列，因此代码量稍大。实际编程中可以使用多
进程中的dummy模块。
"""

from queue import Queue, Empty
from threading import Thread
import requests
from time import time

#自定义全局线程数
THREAD_POOL_SIZE = 10
#设置请求头部
HEADER = {'User-Agent': 'Mozilla/5.0'}
#爬取测试地址
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

#建立队列；在使用多线程时，必须配合其队列一起使用。
def get_html_text(url):
    try:
        r = requests.get(url, headers=HEADER)
        r.raise_for_status
        print('Sucessfully!')
    except:
        print('Failed!')
        
        
def worker(work_queue):
    while not work_queue.empty():
       try:
           url = work_queue.get(block=False)      
       except Empty():
           break
       else:
           get_html_text(url)
           work_queue.task_done()

def main():
    work_queue = Queue()

    for url in URLS:    
       work_queue.put(url)
       
    threads = [Thread(target=worker, args=(work_queue,)) for _ in range(THREAD_POOL_SIZE)]
    for thread in threads:
        thread.start()
    #注意队列堵塞要在线程堵塞之前
    work_queue.join()
    #使用while循环，可以在堵塞线程的同时清空url列表，释放内存。
    #当然也可以使用for循环堵塞，但缺点是无法释放url列表所占内存。
    while threads:
    #此处pop方法承担了两个功能，在返回一个线程对象的同时，删除此对象；此方法极有用。
       threads.pop().join()   
       
 
#测试脚本
if __name__ == '__main__':   
    start = time()
    main()
    end = time()
    print('线程数：{}个\n总耗时：{:.2f} 秒'.format(THREAD_POOL_SIZE,end-start))  
 
