from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = "https://en.wikipedia.org/wiki/Microsoft"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

print("\--------------H2 Categories----------------/")

search4 = page_soup.findAll("h2")
for things in search4:
    result4 = things.text
    print(result4)
    

print("\--------------Loop Search----------------/")

historyStart = page_soup.find("span",{"id":"History"})
findNext = historyStart.find_next(string=True)
findNextAll = historyStart.find_all_next(string=True)

raw_data_list = []
clean_data_list = []
    
for x in findNextAll:
    if x == "Corporate affairs": break
    # print(x)
    # cleanData = x.split(" ", )

    # rawData = re.split(' ',x)
    # for y in rawData:
    #     raw_data_list.append(y)
    
    cleanData = re.findall("[a-zA-Z']+", x)
    # raw_data.append(cleanData)
    for z in cleanData:
        if z:
            # print(cleanData)
            clean_data_list.append(z)
        

# print(clean_data_list)
# print(len(clean_data_list))
# print(raw_data_list)
# print(len(raw_data_list))

# wordstring = 'it was the best of times it was the worst of times '
# wordstring += 'it was the age of wisdom it was the age of foolishness'

# wordlist = wordstring.split()

wordfreq = []
for w in clean_data_list:
    wordfreq.append(clean_data_list.count(w))

# print("String\n" + wordstring +"\n")
# print("List\n" + str(clean_data_list) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(list(zip(clean_data_list, wordfreq))))

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

test = wordListToFreqDict(clean_data_list)
# print(test)

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

test2 = sortFreqDict(test)
print(test2[0])
print(test2[1])
print(test2[2])
print(test2[3])
print(test2[4])
print(test2[5])
print(test2[6])
print(test2[7])
print(test2[8])
print(test2[9])