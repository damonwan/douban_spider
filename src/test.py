#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

from bs4 import BeautifulSoup

f = open('d:\\test\\no_result.txt', encoding='utf-8')
html = f.read()
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('div')
if a:
    print(True)
else:
    print(False)
