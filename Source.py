import requests

page=requests.get("https://www.imdb.com/title/tt5956100/reviews") #fetching reviews from IMDb.com

from bs4 import BeautifulSoup  #web scraping library

soup=BeautifulSoup(page.content,'html.parser')  #parsing html pages

review=soup.find_all(class_="text show-more__control")    # searching for the class and storing the content in variable review

from textblob import TextBlob   #importing textblob for sentiment analysis

positive,negative,neutral=0,0,0
x=0
for i in review:
    text=i.get_text()
    x+=1
    sentiment=TextBlob(text).sentiment.polarity #sentiment lies in between -1 to 1
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
