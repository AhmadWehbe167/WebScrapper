# links = ['/store/apps/details?id=com.farmadventure.global', '/store/apps/details?id=com.farmadventure.global', '/store/apps/dev?id=5790676279664405139', '/store/apps/details?id=com.farmadventure.global', '/store/apps/details?id=games.onebutton.golfstrike', '/store/apps/details?id=games.onebutton.golfstrike', '/store/apps/dev?id=5933611429942957630', '/store/apps/details?id=games.onebutton.golfstrike', '/store/apps/details?id=com.elex.twdsaw.gp', '/store/apps/details?id=com.elex.twdsaw.gp', '/store/apps/dev?id=6711335536439627375', '/store/apps/details?id=com.elex.twdsaw.gp', '/store/apps/details?id=com.supercell.hayday', '/store/apps/details?id=com.supercell.hayday', '/store/apps/dev?id=6715068722362591614', '/store/apps/details?id=com.supercell.hayday', '/store/apps/details?id=com.imangi.templerun2', '/store/apps/details?id=com.imangi.templerun2', '/store/apps/developer?id=Imangi+Studios', 
# '/store/apps/details?id=com.imangi.templerun2']

# for i in range(20):
#     links[i] = "https://play.google.com" + links[i]

# print(links)
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

# myset = {""}

# apps = ['Snapchat', 'Neon Photo Editor - Photo Filters, Collage Maker', 'TikTok', 'TouchRetouch', 'Mimo: Learn coding in JavaScript, Python and HTML', 'Photomath', 'Subway Surfers', 'GIPHY: GIF & Sticker Keyboard & Maker', 'The Zueiras Voice: Text to Speech, Read Aloud TTS', 'Audiomack: Download New Music Offline Free', 'iFunny  fresh memes, gifs and videos', 'Udemy - Online Courses', 'Solar System Scope', 'The Walking Dead: Survivors', 'Duolingo: Learn Languages Free', 'Noteshelf: Take Notes | Handwriting | Annotate PDF', 'Reading Academy! Kids Learn to Read and Write!', 'Photo Lab Picture Editor & Art Face Editing Filter', '9GAG: Funny gifs, pics, fresh memes & viral videos', 'YouTube', 'Family Farm Adventure', 'Golf Strike', 'Toca Life: Office', 'SoloLearn: Learn to Code for Free', 'Daylio - Diary, Journal, Mood Tracker', 'CryptoTab Browser Promine on a PRO level', 'FiLMiC Pro: Professional HD Manual Video Camera', 'Forest: Stay focused', 'Hay Day']

# with open(cwd + '/output/movies.json', 'r') as f:
#     data = json.load(f)
#     for i in range(len(data)):
#         with open(cwd + '/output/movies2.json', 'a') as outfile:
#             data[i]['_id'] = i+29
#             json.dump(data[i], outfile)
#             outfile.write(",")
#     print(myset)

# with open(cwd + "/output/files/app_links.txt", "r") as txt_file:
#     myset = {""}
#     types = txt_file.readlines()
#     for i in range(len(types)):
#         res = types[i].strip('][').replace("\'", "").split(',')
#         temp = []
#         for j in range(len(res)):
#             if(res[j] not in myset):
#                 myset.add(res[j])
#                 with open(cwd + '/output/files/app_links2.txt', 'a') as outfile:
#                     outfile.write(res[j])
                
# apps = ['Snapchat', 'Neon Photo Editor - Photo Filters, Collage Maker', 'TikTok', 'TouchRetouch', 'Mimo: Learn coding in JavaScript, Python and HTML', 'Photomath', 'Subway Surfers', 'GIPHY: GIF & Sticker Keyboard & Maker', 'The Zueiras Voice: Text to Speech, Read Aloud TTS', 'Audiomack: Download New Music Offline Free', 'iFunny  fresh memes, gifs and videos', 'Udemy - Online Courses', 'Solar System Scope', 'The Walking Dead: Survivors', 'Duolingo: Learn Languages Free', 'Noteshelf: Take Notes | Handwriting | Annotate PDF', 'Reading Academy! Kids Learn to Read and Write!', 'Photo Lab Picture Editor & Art Face Editing Filter', '9GAG: Funny gifs, pics, fresh memes & viral videos', 'YouTube', 'Family Farm Adventure', 'Golf Strike', 'Toca Life: Office', 'SoloLearn: Learn to Code for Free', 'Daylio - Diary, Journal, Mood Tracker', 'CryptoTab Browser Promine on a PRO level', 'FiLMiC Pro: Professional HD Manual Video Camera', 'Forest: Stay focused', 'Hay Day']
# with open(cwd + "/output/books.json", "r") as f:
#     data = json.load(f)
#     print(len(data))
    # temp = [(d['title'], d['_id']) for d in data]
    # for i in range(len(temp)):
    #     if(temp[i][0] in apps):
    #         print(temp[i][1])

categories = ["Top-selling comics","Self-Help eBooks","Written by Peter David","Deals on eBooks", "Top-selling eBooks", "More like Mindfulness at Work", "Business & Investing", "Fiction & Literature"]
with open(cwd + "/output/books.json", "r") as txt_file:
    data = json.load(txt_file)
    for i in range(len(data)):
        data[i]['_id'] = 129 + i
        print(i)
        temp = categories[i//10]
        data[i]['group'] = temp
    # for i in range(len(data)):
    with open(cwd + '/output/books2.json', 'a') as outfile:
        json.dump(data, outfile)