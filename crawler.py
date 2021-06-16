from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://en.wikipedia.org/wiki/Microsoft"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

print("\--------------Code Working----------------/")


search = page_soup.findAll("span",{"class":"mw-headline"})
search1 = page_soup.find("span",{"id":"History"})
search2 = page_soup.find("span",{"id":"Corporate_affairs"})
search3 = page_soup.findAll("p")
search4 = page_soup.findAll("h2")

# print(nextThing)

# TODO: This is the latest working code block
# firstThing = page_soup.find("span",{"id":"History"})
# nextThing = firstThing.find_all_next(string=True)
# for stuff in nextThing:
#     result = stuff
#     print(result)

# TODO: I need to create a for loop that runs "find_next" until it reaches id=Corporate_affairs (if id != corporate affairs, stop loop)

for things in search4:
    result4 = things.text
    print(result4)
    
# print(len(search))
# print(search[0])
# print(search[8])

# for stuff in search:
#     result = stuff.string
#     print(result)
    
# for things in search3:
#     result2 = things.text
#     print(result2)
    
print("----------")

# print(search1.contents)
# print(page_soup.p.next_sibling)
# print(search1)
# print(search2)
# print(result)



# print(page_soup.findAll("p"))
# print(page_soup.findAll("p",{"id":"History"}))
# print("h1: ",page_soup.h1.text)

# containers = page_soup.findAll("span",{"id":"History"})
# print(len(containers))

# containers2 = page_soup.findAll("p")
# print(len(containers2))
# print(containers2)