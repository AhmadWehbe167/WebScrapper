import requests
import json
from bs4 import BeautifulSoup
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
categories = ["New & Updated Games","Recommended For You","Laugh Out Loud","Pre-Registration Games", "Just Updated", "Discover Science", "Educational", "Premuim"]

def save_data(app_link, group):
	page = requests.get(app_link)
	soup = BeautifulSoup(page.content, 'html.parser')

	try:
		title = soup.find(class_= 'AHFaub').get_text()
	except Exception as e:
		print("An exception occurred with title: ", e)
		title = ""
	
	try:
		mainImage = soup.select('div.xSyT2c img')[0]['src']
	except Exception as e:
		print("An exception occurred with main image: ", e)
		mainImage = ""

	try:
		genre = [res.get_text() for res in soup.select('span.T32cc')]
	except Exception as e:
		print("An exception occurred with genre: ", e)
		genre= ""
	
	try:
		video = soup.select('div.TdqJUe button')[0]['data-trailer-url']
	except Exception as e:
		print("An exception occurred with video: ", e)
		video = ""

	try:
		images = [res['data-src'] if res.has_attr('data-src') else res['src'] for res in soup.select('button.Q4vdJd img')]
	except Exception as e:
		print("An exception occurred with images: ", e)
		images = ""
	
	try:
		description = soup.find(class_= 'DWPxHb').getText()
	except Exception as e:
		print("An exception occurred with description: ", e)
		description = ""
	
	try:
		more = soup.find_all(class_= 'DWPxHb')[1].getText()
	except Exception as e:
		print("An exception occurred with more: ", e)
		more = ""
	
	try:
		additional = [res.getText() for res in soup.find_all(class_= 'htlgb')]
	except Exception as e:
		print("An exception occurred with additional: ", e)
		additional = ""

	try:
		js = {
			"title": title,
			"mainImage": mainImage,
			"genre": genre,
			"video": video,
			"images": images,
			"description": description,
			"more": more,
			"additional": {
				"updated": additional[0],
				"size": additional[2],
				"installs": additional[4],
				"version": additional[6],
				"requires": additional[8],
				"content": additional[10],
				"elements": additional[12],
				"products": additional[14],
				"permission": additional[16],
				"offeredBy": additional[18],
				"developer": additional[20]
			},
			"group": group
		}
		with open(cwd + '/output/apps.json', 'a') as outfile:
			json.dump(js, outfile)
			outfile.write(",")
	except Exception as e:
		print("An exception occurred: ", e)
		video = ""

with open(cwd + "/output/files/app_links.txt", "r") as txt_file:
	types = txt_file.readlines()
	for i in range(len(types)):
		res = types[i].strip('][').replace("\'", "").split(',')
		for j in range(len(res)):
			save_data(res[j], categories[i])
