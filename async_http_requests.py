# -*- coding: utf-8 -*-

from time import time
import aiohttp
import asyncio


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
    'https://www.hihu.com',
    'http://bbs.pinggu.org/',
    'http://www.tianya.cn/',
    'https://coderprog.com/',
    'https://zooqle.com/',    
]

       
async def get_html_text(url, session):
    #捕获连接异常，这个异常利用assert无法捕获，原因是连接异常发生在session.get
    #阶段，需使用try捕获。
    try:
        async with session.get(url, headers=HEADER) as r:           
            assert r.status == 200
            print('{:50}Sucessfully!'.format(url))
    except:
        print('{:50}Connect Failed!'.format(url))


async def main():
    session = aiohttp.ClientSession()
    #连接时传入session参数。不传也可以，但每个页面请求都需要建立一个session，浪费
    #资源。session本身支持重用，多个连接建议用一个session连接。全部连接任务完成后
    #统一关闭session。
    await asyncio.wait([get_html_text(url, session) for url in URLS])
    await session.close()   
       
 
#测试脚本
if __name__ == '__main__':   
    start = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    end = time()
    print('\n协程：总耗时 {:.2f} 秒'.format(end-start))
    
    
