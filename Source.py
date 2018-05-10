import requests
page=requests.get("https://www.imdb.com/title/tt5956100/reviews")
#page.status_code
#page.content
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify)
review=soup.find_all(class_="text show-more__control")

from textblob import TextBlob
positive,negative,neutral=0,0,0
x=0
for i in review:
    text=i.get_text()
    x+=1
    sentiment=TextBlob(text).sentiment.polarity
    if sentiment > 0:
        positive+=1
    elif sentiment ==0:
        neutral+=1
    elif sentiment < 0:
        negative+=1
print("Positive reviews = ",positive)
print("Neutral reviews = ",neutral)
print("Negative reviews = ",negative)
print("total reviews = ",x)
