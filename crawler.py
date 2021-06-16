from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = "https://en.wikipedia.org/wiki/Microsoft"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

historyStart = page_soup.find("span",{"id":"History"})
findNext = historyStart.find_next(string=True)
findNextAll = historyStart.find_all_next(string=True)

raw_data_list = []
clean_data_list = []
    
for x in findNextAll:
    if x == "Corporate affairs": break
    cleanData = re.findall("[a-zA-Z']+", x)
    for z in cleanData:
        if z:
            clean_data_list.append(z)

wordfreq = []
for w in clean_data_list:
    wordfreq.append(clean_data_list.count(w))

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

test = wordListToFreqDict(clean_data_list)

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

test2 = sortFreqDict(test)

for x in range(10):
    print(test2[x])