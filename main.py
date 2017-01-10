import requests
from bs4 import BeautifulSoup

youtube = "https://www.youtube.com"
# The New Boston channel
url = "https://www.youtube.com/user/thenewboston/playlists"
print("Channel url : " + url)

response = requests.get(url)
html = response.content # All source code of the web page
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

ul = soup.find('ul', attrs={'id': 'channels-browse-content-grid'})
# print(ul)  <ul id="channels-browse-content-grid"></ul>

for li in ul.findAll('li', attrs={'class': 'channels-content-item yt-shelf-grid-item'}):
    # print(li.prettify())
    for a in li.findAll('a', attrs={'class': 'yt-pl-thumb-link'}):
        # print(a.prettify())
        print(a.get('href'))
