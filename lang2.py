#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from langdetect import detect
import csv
import time

#lang = detect("Ein, zwei, drei, vier")


#lang = "川口駅,l"

lang = "haal uyy ooo"


lang = lang.encode('utf8', 'ignore').decode('utf8')

langu = detect(lang)


#rev = rev.encode('ascii', 'ignore').decode('ascii')

print langu
#output: de

file_name = "Hotels_Restaurants_in_Japan_by_name.csv"

with open(file_name) as f:
        ####content = f.readlines()
        content=csv.reader(f)
        for row in content:
            print(row)
            try:

                #in case dealing with the by name file (which has list of items, so i merge them firstly
                ###row[0] = row[0] + " ; " + row[1] + " ; " + row[2] + " ; " + row[3] + "."
                row[0] = row[0].encode('utf8', 'ignore').decode('utf8')
                langu = detect(row[0])
                #rev = rev.encode('ascii', 'ignore').decode('ascii')
                print langu
                if langu == "en":
                    print("English line")
                    time.sleep(4)
            
        

                    # you may also want to remove whitespace characters like `\n` at the end of each line
                    ###row[0] = [x.strip() for x in row[0]] 
                    row[0] = row[0].strip('\n')
                    row[0] = row[0].replace('\n','')
                    row[0] = row[0] + "."
                    print(row[0])
                    time.sleep(4)
                    #write line to file
                    writer.writerow(row[0])



                else:
                    print("Not English line")


            except:
                print("******************problem***********")

