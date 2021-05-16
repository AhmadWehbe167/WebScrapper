import requests
import json
from bs4 import BeautifulSoup
import os 

# page = requests.get("")
# soup = BeautifulSoup(page.content, 'html.parser')

rooturl='https://play.google.com/store/books/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfZnJlZRAHGAE%3D:S:ANO1ljKG7Lo&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19mcmVlEAcYAQ%3D%3D:S:ANO1ljLtUdw'
with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }
    resp = se.get(rooturl)
soup = BeautifulSoup(resp.content,"html.parser")

try:
    title = ['https://play.google.com' + res['href'] for res in soup.select('div.f5NCO a')[:40]]
except Exception as e:
    print("An exception occurred: ", e)

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

with open(cwd + '/output/files/books_links.txt', 'a') as outfile:
    outfile.write(str(title))
    outfile.write('\n')