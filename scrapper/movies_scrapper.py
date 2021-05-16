import requests
import json
from bs4 import BeautifulSoup
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
categories = ["New Movies","Top-Selling Movies","Recommended For You","New rental movies","Superhero movies","Comedy drama movies","Laugh out loud movies","Thrilling movies"]

def save_data(app_link, group, myid):
    with requests.Session() as se:
        se.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }
        resp = se.get(app_link)
    soup = BeautifulSoup(resp.content,"html.parser")

    try:
        title = soup.select('.AHFaub span')[0].get_text()
    except Exception as e:
        print("An exception occurred with title: ", e)
        print("link is: ", app_link)
        title = ""

    try:
        mainImage = soup.select('div.hkhL9e img')[0]['src']
    except Exception as e:
        print("An exception occurred with main image: ", e)
        print("link is: ", app_link)
        mainImage = ""

    try:
        price = soup.select('span.oocvOe button')[0]['aria-label']
        price = price.replace("\u00a0", " ")
    except Exception as e:
        print("An exception occurred with price: ", e)
        print("link is: ", app_link)
        price = ""
    
    try:
        yearProduced = soup.find_all(class_= 'UAO9ie')[0].get_text()
    except Exception as e:
        print("An exception occurred with year produced: ", e)
        print("link is: ", app_link)
        yearProduced = ""

    try:
        duration = soup.find_all(class_= 'UAO9ie')[1].get_text()
    except Exception as e:
        print("An exception occurred with duration: ", e)
        print("link is: ", app_link)
        duration = ""

    try:
        genre = [res.get_text() for res in soup.select('a.hrTbp.R8zArc')]
    except Exception as e:
        print("An exception occurred with genre: ", e)
        print("link is: ", app_link)
        genre= ""

    try:
        video = soup.select('div.TdqJUe button')[0]['data-trailer-url']
    except Exception as e:
        print("An exception occurred with video: ", e)
        print("link is: ", app_link)
        video = ""

    try:
        description = soup.find(class_= 'DWPxHb').getText()
    except Exception as e:
        print("An exception occurred with description: ", e)
        print("link is: ", app_link)
        description = ""

    try:
        actors = soup.find(class_= 'VSl7Ie').getText()
    except Exception as e:
        print("An exception occurred with actors: ", e)
        print("link is: ", app_link)
        actors = ""
    
    try:
        producers = soup.find_all(class_= 'VSl7Ie')[1].getText()
    except Exception as e:
        print("An exception occurred with producers: ", e)
        print("link is: ", app_link)
        producers = ""

    try:
        directors = soup.find_all(class_= 'hrTbp')[2].getText()
    except Exception as e:
        print("An exception occurred with directors: ", e)
        print("link is: ", app_link)
        directors = ""

    try:
        quality = soup.find(class_= 'htlgb').getText()
    except Exception as e:
        print("An exception occurred with quality: ", e)
        print("link is: ", app_link)
        quality = ""

    try:
        audioLanguage = soup.find_all(class_= 'htlgb')[1].getText()
    except Exception as e:
        print("An exception occurred with audio language: ", e)
        print("link is: ", app_link)
        audioLanguage = ""

    try:
        subtitles = soup.find_all(class_= 'htlgb')[2].getText()
    except Exception as e:
        print("An exception occurred with subtitles: ", e)
        print("link is: ", app_link)
        subtitles = ""

    try:
        movie = {
            "_id": myid,
            "app_link": app_link,
            "title": title,
            "mainImage": mainImage,
            "yearProduced":yearProduced ,
            "duration": duration,
            "price": price,
            "genre": genre,
            "video": video,
            "description": description,
            "actors": actors,
            "producers": producers,
            "director": directors,
            "additional": {
                "quality": quality,
                "audioLanguage": audioLanguage,
                "subtitles": subtitles
            },
            "group": group
        }
        with open(cwd + '/output/movies.json', 'a') as outfile:
            json.dump(movie, outfile)
            outfile.write(",")
    except Exception as e:
        print("An exception occurred: ", e)
        print("link is: ", app_link)
    
    try:
        reviews = {
            "_id": myid,
            "app_link":app_link,
            "totalScore": "String",
            "totalStars": 0,
            "fiveWidth": 0,
            "fourWidth": 0,
            "threeWidth": 0,
            "twoWidth": 0,
            "oneWidth": 0,
            "total": "String",
            "reviews": [
                {
                "name": "String",
                "profile": "String",
                "stars": 0,
                "date": "String",
                "likes": "String",
                "review": "String"
                }
            ]
        }
        with open(cwd + '/output/movies.json', 'a') as outfile:
            json.dump(movie, outfile)
            outfile.write(",")
    except Exception as e:
        print("An exception occurred: ", e)
        print("link is: ", app_link)   



# with open(cwd + "/output/files/movies_links.txt", "r") as txt_file:
#     types = txt_file.readlines()
#     for i in range(2 , len(types)):
#         res = types[i].strip('][').replace("\'", "").split(',')
#         for j in range(len(res)):
#             save_data(res[j], categories[i])