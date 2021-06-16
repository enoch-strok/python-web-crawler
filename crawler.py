from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = "https://en.wikipedia.org/wiki/Microsoft"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


# //------------------ Adjust Here ------------------ //
words_to_display = 10
words_to_exclude = 'put_some_words_in_here'
# //------------------ Adjust Here ------------------ //


page_soup = soup(page_html, "html.parser")

historyStart = page_soup.find("span",{"id":"History"})
findNext = historyStart.find_next(string=True)
findNextAll = historyStart.find_all_next(string=True)

clean_data_list = []
    
for x in findNextAll:
    if x == "Corporate affairs": break
    cleanData = re.findall("[a-zA-Z']+", x)
    for z in cleanData:
        if z and z != words_to_exclude:
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

def final_return(x):
    print(x)
    return x

def final_results(y):
    for x in range(words_to_display):
        final_return(y[x])

final_results(test2)
