import requests
import json
from bs4 import BeautifulSoup
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
# apps = ['Snapchat', 'Neon Photo Editor - Photo Filters, Collage Maker', 'TikTok', 'TouchRetouch', 'Mimo: Learn coding in JavaScript, Python and HTML', 'Photomath', 'Subway Surfers', 'GIPHY: GIF & Sticker Keyboard & Maker', 'The Zueiras Voice: Text to Speech, Read Aloud TTS', 'Audiomack: Download New Music Offline Free', 'iFunny  fresh memes, gifs and videos', 'Udemy - Online Courses', 'Solar System Scope', 'The Walking Dead: Survivors', 'Duolingo: Learn Languages Free', 'Noteshelf: Take Notes | Handwriting | Annotate PDF', 'Reading Academy! Kids Learn to Read and Write!', 'Photo Lab Picture Editor & Art Face Editing Filter', '9GAG: Funny gifs, pics, fresh memes & viral videos', 'YouTube', 'Family Farm Adventure', 'Golf Strike', 'Toca Life: Office', 'SoloLearn: Learn to Code for Free', 'Daylio - Diary, Journal, Mood Tracker', 'CryptoTab Browser Promine on a PRO level', 'FiLMiC Pro: Professional HD Manual Video Camera', 'Forest: Stay focused', 'Hay Day']

# def save_data(app_link):
#     headers = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
#     page = requests.get(app_link, headers=headers)
#     soup = BeautifulSoup(page.content, 'html.parser')

    # try:
    #     title = soup.find(class_= 'AHFaub').get_text()
    #     if(title not in apps):
    #         return False
    #     else:
    #         for i in range(len(temp)):
    #             if(temp[i][0] in apps):
    #                 myid = temp[i][1]
    # except Exception as e:
    #     print("An exception occurred with title: ", e)
    #     title = ""
        
    # try:
    #     totalScore = soup.find(class_= 'BHMmbe').get_text()
    # except Exception as e:
    #     print("An exception occurred with totalScore: ", e)
    #     totalScore = ""
    
    
    # print(totalScore)
        
    # try:
    #     total = soup.find(class_= 'EymY4b').get_text()
    # except Exception as e:
    #     print("An exception occurred with total: ", e)
    #     total = ""
    
    # try:
    #     mainImage = soup.select('div.xSyT2c img')[0]['src']
    # except Exception as e:
    #     print("An exception occurred with main image: ", e)
    #     mainImage = ""

    # try:
    #     genre = [res.get_text() for res in soup.select('span.T32cc')]
    # except Exception as e:
    #     print("An exception occurred with genre: ", e)
    #     genre= ""

    # try:
    #     video = soup.select('div.TdqJUe button')[0]['data-trailer-url']
    # except Exception as e:
    #     print("An exception occurred with video: ", e)
    #     video = ""

    # try:
    #     userName = soup.find(class_= 'd15Mdf')
    # except Exception as e:
    #     print("An exception occurred with userName: ", e)
    #     userName = ""
    
    
    # print(userName)

    # try:
    #     js = {
    #         "_id": myid,
    #         "totalScore": totalScore,
    #         "total": total,
    #         "reviews": [
    #             {
    #             "name": "String",
    #             "profile": "String",
    #             "stars": 0,
    #             "date": "String",
    #             "likes": "String",
    #             "review": "String"
    #             }
    #         ]
    #         }
    #     with open(cwd + '/output/apps.json', 'a') as outfile:
    #         json.dump(js, outfile)
    #         outfile.write(",")
    # except Exception as e:
    #     print("An exception occurred: ", e)
    #     video = ""

# with open(cwd + "/output/files/app_links.txt", "r") as txt_file:
#     types = txt_file.readlines()
#     with open(cwd + "/output/apps.json", "r") as f:
#         data = json.load(f)
#         temp = [(d['title'], d['_id']) for d in data]
#     for i in range(len(types)):
#         res = types[i].strip('][').replace("\'", "").split(',')
#         for j in range(len(res)):
#             save_data(res[j], temp)
# save_data('https://play.google.com/store/apps/details?id=com.playrix.farmscapes')

data = [{
    "_id": 0,
    "totalScore": "4.5",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "Livadia",
        "profile": "https://play-lh.googleusercontent.com/a/AATXAJzr4YIt0ZFDx1uaSzZQbYn-bnrpcjIS4iDcrmIw=w48-h48-n-rw-mo",
        "stars": 1,
        "date": "28 April 2021",
        "likes": "43",
        "review": "Big disappointment. It's a blast game not Match3. Graphics are beautiful as usual for Playrix but there is a catch...difficulty of levels. I don't need a challenge I need a lot of fun. There are so many games to play I can't waste my time trying to get through levels much less spend money to do so."
      }
    ]
  },
  {
    "_id": 1,
    "totalScore": "4",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "April Morgan",
        "profile": "https://play-lh.googleusercontent.com/a-/AOh14GjNfIsrsdzBQ5GNiyAU1CBn_KRBYPy-bLd22d0X5w=w48-h48-n-rw",
        "stars": 5,
        "date": "28 April 2021",
        "likes": "42",
        "review": "The reason that I'm giving this 4 ⭐'s is because there is still some kinks in the game that needs to be worked out and I have a suggestion for the game. Can you please add teammates to this game like you have for Homescapes and Gardenscapes? Also, you need to find away that players can be able to send lives or receive lives from each other. Other than that, it's a good game"
      }
    ]
  },
  {
    "_id": 2,
    "totalScore": "3.5",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "Pauline Walls",
        "profile": "https://play-lh.googleusercontent.com/a-/AOh14Gj4Fm671mA2-tsA54Yi5Uimi3iF1tPxQBo20GoUcA=w48-h48-n-rw",
        "stars": 4,
        "date": "29 April 2021",
        "likes": "36",
        "review": "Someone call tech support 📞 This game won't even open, saying I need internet access in order to play it despite having a clear wifi signal and full bars. It doesn't make sense. Neither data nor wifi seems to enable me to play it. I can't give it more that 1 star simply because I can't even access the game. Until this changes, my rating remains. Hopefully it works for other people."
      }
    ]
  },
  {
    "_id": 3,
    "totalScore": "3.5",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "Noah Fultz",
        "profile": "https://play-lh.googleusercontent.com/a-/AOh14GhQBwFunElpj0AzOQ6yRji9hX_QONGEOUAl8Ibwhg=w48-h48-n-rw",
        "stars": 1,
        "date": "27 April 2021",
        "likes": "54",
        "review": "Someone call tech support 📞 This game won't even open, saying I need internet access in order to play it despite having a clear wifi signal and full bars. It doesn't make sense. Neither data nor wifi seems to enable me to play it. I can't give it more that 1 star simply because I can't even access"
      }
    ]
  },
  {
    "_id": 4,
    "totalScore": "3.5",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "Shreyas Ranjan",
        "profile": "https://play-lh.googleusercontent.com/a-/AOh14GhvrR0L3cJ4UKeO_O9O4CBXKA8nMN42EwZhdlA=w48-h48-n-rw",
        "stars": 4,
        "date": "28 April 2021",
        "likes": "4",
        "review": "I have played all the games of plarix but this was the best game I have ever played it has excellent graphics , a intersting story and good characters the levels are also not so hard but I have a problem that when I go to the task menu sometimes there is written \"to continue the game exit the game as"
      }
    ]
  },
  {
    "_id": 5,
    "totalScore": "3.5",
    "total": "4,369 total",
    "reviews": [
      {
        "name": "Tatenda Manyarara",
        "profile": "https://play-lh.googleusercontent.com/a-/AOh14GjDNzMQ-fpbUz3bZMYIeaH0As3yjwGgsEH9h5yJmg=w48-h48-n-rw",
        "stars": 4,
        "date": "27 April 2021",
        "likes": "1",
        "review": "The game keeps stopping in the middle of me playing it saying that it's open on another device and I need to close it on the other device first but 1. I've literally never played the game before. 2. I don't own another device but my phone. It seems like a good game so far from what I've been able to play though."
      }
    ]
  }]

with open(cwd + "/output/reviews2.json", "a") as outfile:
    counter = 0
    for i in range(1, 35):
        for j in range(1, 7):
            data[j-1]['_id'] = counter
            counter += 1
            json.dump(data[j-1], outfile)
            outfile.write(",")