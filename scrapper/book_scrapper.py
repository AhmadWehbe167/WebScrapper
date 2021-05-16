import requests
import json
from bs4 import BeautifulSoup
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
categories = ["Top-selling comics","Self-Help eBooks","Written by Peter David","Deals on eBooks", "Top-selling eBooks", "More like Mindfulness at Work", "Business & Investing", "Fiction & Literature"]

def save_data(app_link, group):
	page = requests.get(app_link)
	soup = BeautifulSoup(page.content, 'html.parser')

	try:
		title = soup.find(class_= 'AHFaub').get_text()
	except Exception as e:
		print("An exception occurred with title: ", e)
		title = ""
	
	try:
		mainImage = soup.select('div.hkhL9e img')[0]['src']
	except Exception as e:
		print("An exception occurred with main image: ", e)
		mainImage = ""

	try:
		genre = [res.get_text() for res in soup.select('a.R8zArc')]
	except Exception as e:
		print("An exception occurred with genre: ", e)
		genre= ""
	
	try:
		description = soup.find(class_= 'DWPxHb').getText()
	except Exception as e:
		print("An exception occurred with description: ", e)
		description = ""
	
	try:
		creator = soup.select('div.uN7Lic span')[0].getText()
	except Exception as e:
		print("An exception occurred with creator: ", e)
		creator = ""

	try:
		date = soup.select('span.T32cc')[0].getText()
	except Exception as e:
		print("An exception occurred with date : ", e)
		date = ""

	try:
		price = soup.select('span.oocvOe button')[0]['aria-label']
	except Exception as e:
		print("An exception occurred with price: ", e)
		price = ""
    
	try:
		more = soup.select('div.JHTxhe')[2].getText()
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
			"_id": 0,
			"title": title,
			"mainImage": mainImage,
			"creator": creator,
			"date": date,
			"genre": genre,
			"price": price,
			"description": description,
			"more": more,
			"additional": {
				"publisher": additional[0],
				"published on": additional[1],
				"pages": additional[2],
				"ISBN": additional[3],
				"features": additional[4],
    			"bestfor": additional[5],
				"language": additional[6]
			},
			"group": group
			}
		with open(cwd + '/output/books.json', 'a') as outfile:
			json.dump(js, outfile)
			outfile.write(",")
	except Exception as e:
		print("An exception occurred: ", e)

with open(cwd + "/output/files/books_links.txt", "r") as txt_file:
	types = txt_file.readlines()
	for i in range(len(types)):
		res = types[i].strip('][').replace("\'", "").split(',')
		for j in range(len(res)):
			save_data(res[j], categories[i])