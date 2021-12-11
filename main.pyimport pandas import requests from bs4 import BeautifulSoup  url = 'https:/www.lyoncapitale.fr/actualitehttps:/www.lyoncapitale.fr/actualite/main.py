import pandas
import requests
from bs4 import BeautifulSoup

url = 'https://www.lyoncapitale.fr/actualitehttps://www.lyoncapitale.fr/actualite/'
start_with_word = 'actualite'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser').find_all('a')
trash_url_list = []

for i in soup:
    if str(i).startswith('http'):
        trash_url_list.append(i.get('href'))
    else:
        trash_url_list.append(url + str(i.get('href')))

x = pandas.DataFrame(trash_url_list)
z = []

for i in x.values:
    if i[0] not in z:
        z.append(i[0])

a = pandas.DataFrame(z)
b = []
links = []
for i in a.values:
    if str(i[0][103:-1]).startswith(start_with_word):
        b.append(str(i[0][113:]).capitalize())
        links.append(i[0])

c = []
for i in b:
    c.append(i.replace('-', ' '))
    print(c[b.index(i)])
    print(links[b.index(i)])

csv = pandas.DataFrame({'name': c, 'link': links})
csv.to_csv('output_lyon_capitale.csv')
print(len(b), 'news outputted')
