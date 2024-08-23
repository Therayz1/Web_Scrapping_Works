import requests
from bs4 import BeautifulSoup

link = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
kod = requests.get(link, headers=headers).content
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Web sitesine erişim sağlanamadı. HTTP hata kodu:", response.status_code)


parser = BeautifulSoup(kod,"html.parser")
li = parser.find("ul",{"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"}).find_all("li")
for i in li:
    baslik = i.find("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-4dcdad14-9 dZscOy cli-title"}).find("a").string
    print(baslik)
