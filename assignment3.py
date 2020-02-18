#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 3

from __future__ import division
import csv
import urllib2
import re
import argparse
import sys




parser = argparse.ArgumentParser(description='--url argument')
parser.add_argument("--url", required = True, help = "URL to get site data. Required")
args = parser.parse_args()
url = urllib2.Request(args.url)
pgopen = urllib2.urlopen(url)
csr = csv.reader(pgopen)
    

    
tHITS = 0
IMGt = 0
nFF = 0
nCH = 0
nIE = 0
nSF = 0





for row in csr:
    tHITS += 1
    IMGC = re.search(r'(\.(jpg|gif|png))', row[0], flags = re.I)
    FFC = re.search(r'(firefox)', row[2], flags = re.I)
    CHC = re.search(r'(chrome)', row[2], flags = re.I)
    IEC = re.search(r'(MSIE)', row[2])
    SFC = re.search(r'(safari)', row[2], flags = re.I)
    if IMGC > 0:
        IMGt += 1
    if FFC > 0:
        nFF += 1
    if CHC > 0:
        nCH += 1
    if IEC > 0:
        nIE += 1
    if SFC > 0:
        nSF += 1


tIMGR = (IMGt/tHITS)*100
lbrowsers = [[1,nFF],[2,nCH],[3,nIE],[4,nSF]]
dictBROWSERS = dict(lbrowsers)

pBROWSER = None

compare = max(dictBROWSERS, key=dictBROWSERS.get)
if compare == 1:
    pBROWSER = "Firefox"
if compare == 2:
    pBROWSER = "Chrome"
if compare == 3:
    pBROWSER = "Internet Explorer"
if compare == 4:
    pBROWSER = "Safari" 


print "Image requests account for {}% of all requests.".format(tIMGR)
print "The most popular browser accessing ths site is {}.".format(pBROWSER)









