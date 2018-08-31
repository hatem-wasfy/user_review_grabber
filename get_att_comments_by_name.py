#!/usr/bin/python2
import requests
import csv
import pprint

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#######

import sys  
import importlib
import imp
import json
import time
cities =[]
with open('cities.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        x = p['country']
        if x == 'JP':
            ###print('Country: ' + p['country'])
            ###print('City: ' + p['name'])
            #print('From: ' + p['from'])
            print('')
            xname = p['name']
            print(xname)

            xname = xname.encode('ascii', 'ignore').decode('ascii')
            ###cities.append(p['name'])
            cities.append(xname)
#######



cities = sorted(cities)
atts = ["hotels", "restaurants"]

for att in atts:
    print('Now working on the attraction of: ' + att)
    for city in cities:
        print('Writing user reviews for City: ' + city)
        
        ###city = "Tokyo"

        #att = "hotels or restaurants"
        ###attraction_string = "restaurants, " + city
        attraction_string = att + ", " + city

        file_name = "Hotels_Restaurants_in_Japan_by_name.csv"
        ###file_name = att + "_in_Japan.csv"
        
        #sending get request.
        main_api = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        parameters = {"query":attraction_string,
                    "key":""} #enter api key here.
        resp = requests.get(main_api, parameters).json()
        
        #it selects the places with at least one rating, and puts their place id in place_id.
        place_id = [result['place_id'] for result in resp['results'] if 'rating' in result]
        
        #creating a csv file and with headings.
        with open(file_name, "a+") as toWrite:
            writer=csv.writer(toWrite)
            ###writer.writerow(['Date Collected',  'Health Care Provider', 'HCP location', 'Website Review is From', 'Specialty', 'Reviewer Name',\
                ###'Date of Review', 'Reviewer Demographics(gender/race)', 'Star Rating', 'How Many Stars', 'Other Meta-Data', 'Review', 'URL'])
            #getting responses using place ids collected in place_id.
            for ids in place_id:
                details_api = "https://maps.googleapis.com/maps/api/place/details/json?"
                parameters = {"placeid": ids,
                            "key":"" } #api key here.
                detail_resp = requests.get(details_api, parameters)
                result = detail_resp.json()['result']
                try:
                    reviewss = result['reviews']
                    doc_name=result['name']
                    doc_url = result['url']
                    city_state = result['formatted_address']
                    website = 'GOOGLE'
                    specialty = 'Urologists'
                    date_collected = 'June 15 2017'
                    total_poss = '5'
                    #gets multiple reviews of the physician(if any).
                    for review in reviewss:
                        ###rating = review['rating']
                        ###revname = review['author_name']
                        rev = review['text']
                        ###date_review = review['relative_time_description']
                        ###rev_url = review.get('author_url', '')
                        
                        ##yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')
                        rev = rev.encode('ascii', 'ignore').decode('ascii')
                        ###revname = revname.encode('ascii', 'ignore').decode('ascii')
                        ###date_review = date_review.encode('ascii', 'ignore').decode('ascii')
                        ###rev_url = rev_url.encode('ascii', 'ignore').decode('ascii')

            


                        ###writer.writerow([date_collected, doc_name, city_state, website, specialty, revname, date_review, rev_url, rating, total_poss, '', rev, doc_url])

                        writer.writerow([city,att,doc_name,rev, '.'])
                        ###writer.writerow([rev, '.'])


                except:
                    print('******** WARNING: No reviews are found for this city: ' + city)
