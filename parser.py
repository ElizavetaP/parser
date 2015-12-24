## -*- coding: utf-8 -*-
import urllib.request
import lxml.html
import sys
import configparser
from urllib.parse import urlparse

config = configparser.RawConfigParser()
config.read('config.ini')

if len(sys.argv) == 1:
    print('enter url')
    sys.exit(1)

section = urlparse(sys.argv[1]).netloc

try:
    charset = config.get(section, 'charset')
except Exception:
    print('Unknown domain')
    sys.exit(1)
rawpage = urllib.request.urlopen(sys.argv[1]).read().decode(charset)
    
page = lxml.html.document_fromstring(rawpage)

def getfile(url):
    filename = ''
    i = 2
    while i < len(url):
        if url[i-2]==url[i-1]=='/':
            for c in str(url[i:]):
                if c != '/':
                    filename = filename +c
                else:
                    filename = filename +'_'
            break
        i = i + 1
    return filename + ".txt"

file = open(getfile(sys.argv[1]), 'w')

def writeline(text):
    text = (text.split())
    l = 0
    while l < len(text):
        i = 1
        if len(text[l])>80:
                file.write(text[l])
                file.write('\n')
                i = 1
                l = l + 1
        else:
            while  l < len(text) and i + len(text[l])<80:
                if len(text[l])>80:
                    file.write(text[l])
                    file.write('\n')
                    i = 1
                        
                else:
                    file.write(text[l]+' ')
                    i = i + len(text[l])+1
                l = l + 1
            file.write('\n')
    file.write('\n')
        
def printhead(headpath):
    head=page.xpath(headpath)[0]
    writeline(head)
    file.write('\n')
        
def printtext(tagpath):
    for paragraph in page.xpath(tagpath):
        w = paragraph.xpath('text() | *//@href | *//text()')
        i = 0
        par = ''
        while i < len(w):
            if 'http' in w[i]:
                par +=' [' + w[i] + '] '
            else:
                par += w[i]
            i = i + 1
        writeline(par)


printhead(config.get(section, 'head'))
printtext(config.get(section, 'tag'))
file.close()
