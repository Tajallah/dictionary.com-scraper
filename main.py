from urllib.request import urlopen
from bs4 import BeautifulSoup as beausu

dicc = urlopen('http://www.dictionary.com/')

soup = beausu(dicc, 'html.parser')

wotd = soup.find(id='wotdAudio-play').get('href')

dicc = urlopen(wotd)

soup = beausu(dicc, 'html.parser')

word = soup.h1.text
alt_spellings = soup.h3.text
pos = [item.text for item in soup.find_all(class_='luna-pos')]
defs = [item.text for item in soup.find_all(class_='css-9sn2pa e10vl5dg6')]

print(word)
print(alt_spellings)
print(pos)
print(defs)
