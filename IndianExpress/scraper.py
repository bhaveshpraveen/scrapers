import requests
from bs4 import BeautifulSoup


def tech():
    url = 'http://indianexpress.com/section/technology/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    var1 = soup.find_all("ul", {"class": "article-list"})[0]
    for i in var1:
        try:
            print(i.h3.a.text)  # the title
        except:
            pass
        try:
            print(i.h3.a.get("href"))  # the link to the article
        except:
            pass
        try:
            print(i.figure.a.img.get("src"))  # the link to the image of the article
        except:
            pass
        print()


def sports():
    url = 'http://indianexpress.com/section/sports/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    var1 = soup.find_all("div", {'class': ['articles', 'articles first']})
    for i in var1:
        try:
            print(i.div.next_sibling.a.text)  # title
        except:
            pass
        try:
            print(i.div.a.get("href"))  # news link
        except:
            pass
        try:
            print(i.div.a.img.get("src"))  # image
        except:
            pass
        print()


def travel():
    url = 'http://indianexpress.com/section/lifestyle/destination-of-the-week/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    var1 = soup.find_all("div", {'class': ['articles', 'articles first']})
    for i in var1:
        try:
            print(i.div.next_sibling.a.text)  # title
        except:
            pass
        try:
            print(i.div.a.get("href"))  # news link
        except:
            pass
        try:
            print(i.div.a.img.get("src"))  # image
        except:
            pass
        print()


def food():
    url = 'http://indianexpress.com/section/lifestyle/food-wine/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    var1 = soup.find_all("div", {'class': 'articles'})
    for i in var1:
        try:
            print(i.div.next_sibling.a.text)  # title
        except:
            pass
        try:
            print(i.div.a.get("href"))  # news link
        except:
            pass
        try:
            print(i.div.a.img.get("src"))  # image
        except:
            pass
        print()


def entertainment():
    url = 'http://indianexpress.com/section/entertainment/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    var1 = soup.find_all("div", {'class': ['articles', 'articles first']})
    for i in var1:
        try:
            print(i.div.next_sibling.a.text)  # title
        except:
            pass
        try:
            print(i.div.a.get("href"))  # news link
        except:
            pass
        try:
            print(i.div.a.img.get("src"))  # image
        except:
            pass
        print()

tech()
sports()
travel()
food()
entertainment()
