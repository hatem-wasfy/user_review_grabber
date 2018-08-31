#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from langdetect import detect

#lang = detect("Ein, zwei, drei, vier")


#lang = "川口駅,l"

lang = "haal uyy ooo"


lang = lang.encode('utf8', 'ignore').decode('utf8')

langu = detect(lang)


#rev = rev.encode('ascii', 'ignore').decode('ascii')

print langu
#output: de
