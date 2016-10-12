#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2016年10月9日

@author: wanmaosheng
'''

import mysql.connector
import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import re
import requests

# def get_conn():
#     host = '10.128.160.50'
#     user = 'tddl_user'
#     password = 'Tdl01'
#     database = 'movie'
#     return mysql.connector.connect(host=host, user=user, password=password, database=database)
#     
# async def wget(url):
#     async with ClientSession() as session:
#         with (await sem):
#             headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
#             async with session.get(url, headers=headers, compress=True) as response:
#                 print('get', url, 'status is', response.status)
#                 if (response.status != 200):
#                     save_error_log(str(response.status) + "  " + url)
#                 try:
#                     result = await response.read()
#                 finally:
#                     await response.release()
#                     
#                 if result:
#                     try:
#                         parse(result)
#                     except BaseException as e:
#                         print(e)
#                         save_error_log(result)
#             
# async def run(tasks):
# #     url = 'https://movie.douban.com/tag/2016?start={}'
# #     for i in range(0, 6000, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#         
# #     url = 'https://movie.douban.com/tag/2015?start={}'
# #     for i in range(0, 3000, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
# 
# #     url = 'https://movie.douban.com/tag/2014?start={}'
# #     for i in range(1600, 2200, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2013?start={}'
# #     for i in range(0, 2000, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2012?start={}'
# #     for i in range(0, 1600, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2011?start={}'
# #     for i in range(800, 1400, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2010?start={}'
# #     for i in range(0, 1300, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2009?start={}'
# #     for i in range(0, 1200, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2008?start={}'
# #     for i in range(0, 1000, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2007?start={}'
# #     for i in range(0, 1000, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2006?start={}'
# #     for i in range(0, 900, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#          
# #     url = 'https://movie.douban.com/tag/2005?start={}'
# #     for i in range(0, 800, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#         
# #     url = 'https://movie.douban.com/tag/2004?start={}'
# #     for i in range(0, 600, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)
#         
# #     url = 'https://movie.douban.com/tag/2003?start={}'
# #     for i in range(0, 520, 20):
# #         task = asyncio.ensure_future(wget(url.format(i)))
# #         tasks.append(task)    
#          
#     url1 = 'https://movie.douban.com/tag/2002?start={}'
#     for i in range(0, 480, 20):
#         task = asyncio.ensure_future(wget(url1.format(i)))
#         tasks.append(task)    
#          
#     url2 = 'https://movie.douban.com/tag/2001?start={}'
#     for i in range(0, 440, 20):
#         task = asyncio.ensure_future(wget(url2.format(i)))
#         tasks.append(task)       
#      
#     url3 = 'https://movie.douban.com/tag/2000?start={}'
#     for i in range(0, 400, 20):
#         task = asyncio.ensure_future(wget(url3.format(i)))
#         tasks.append(task)
#         
# def save_item(item):
#     item_id = item['id']
#     name = item['name']
#     url = item['url']
#     rating = item['rating']
#     numbers = item['numbers']
#     cursor = conn.cursor()
#     cursor.execute('insert into item (item_id, name, url, rating, numbers) values (%s, %s, %s, %s, %s)', [item_id, name, url, rating, numbers])
#     conn.commit()
#     
# def save_error_log(log):
#     cursor = conn.cursor()
#     cursor.execute('insert into html (content) values (%s)', [log,])
#     conn.commit()
# 
# def parse(result):
#     html = result.decode('utf-8')
#     soup = BeautifulSoup(html, 'html.parser')
#     tr_list = soup.select('tr.item')
#     for tr in tr_list:
#         item = {}
#         item['url'] = tr.a['href']
#         item['id'] = re.findall(re_id, item['url'])[0]
#         item['name'] = tr.a['title']
#         if tr.select('span.rating_nums'):
#             for s in tr.select('span.rating_nums')[0].stripped_strings:
#                 item['rating'] = str(s)
#         else:
#             item['rating'] = None
#         if tr.select('span.pl'):
#             for s in tr.select('span.pl')[0].stripped_strings:
#                 replace_str = re.findall(re_id, str(s))
#                 if replace_str:
#                     item['numbers'] = replace_str[0]
#                 else:
#                     item['numbers'] = None
#         else:
#             item['numbers'] = None
#         try:
#             save_item(item)
#         except BaseException as e:
#             print(e)
# #             save_error_log(item['id'] + item['name'])

# re_id = re.compile(r'(\d+)')
# tasks = []
# conn = get_conn()
# sem = asyncio.Semaphore(20)
# loop = asyncio.get_event_loop()
# future = asyncio.ensure_future(run(tasks))
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Host': 'book.douban.com',
           'Referer': 'https://book.douban.com/',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
           }



r = requests.get(url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all')
print(r.status_code)    # 获取返回状态
print(r.url)
print(r.text)   #打印解码后的返回数据


tags = re.findall('<td><a href="/tag/(.*?)">', r.text, re.S)
for tag in tags:
    print(tag)


if __name__ == '__main__':
    pass