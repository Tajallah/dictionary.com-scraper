from urllib.request import urlopen
from bs4 import BeautifulSoup as beausu

class wotd:
        word = ''
        alt_spellings = ''
        pos = []
        defs = []

        def __init__(self):
                dicc = urlopen('http://www.dictionary.com/')
                soup = beausu(dicc, 'html.parser')

                wotd = soup.find(id='wotdAudio-play').get('href')

                dicc = urlopen(wotd)

                soup = beausu(dicc, 'html.parser')

                self.word = soup.h1.text
                self.alt_spellings = soup.h3.text
                self.pos = [item.text for item in soup.find_all(class_='luna-pos')]
                self.defs = [item.text for item in soup.find_all(class_='css-9sn2pa e10vl5dg6')]

        def format(self):
                output = ''
                output += '**' + self.word + '**\n\n'
                output += '[' + self.alt_spellings + ']\n\n'
                for item in self.pos:
                        output += item + '\n' #todo find cases of multiple POS and add handling for them
                output += '\n'
                for item in self.defs:
                        output += '*\'' + item +'*\'\n'
                return output
