
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pandas as pd

 
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)
    image_data={}

#grab title and text
    url ='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
    news_title= soup.find_all('div', class_='content_title')
    news_title= news_title[1].a.text
    news_p = soup.find_all('div', class_='article_teaser_body')
    news_p = news_p[0].text
    #Add title and text to image data
    image_data["news_title"]=news_title
    image_data["news_p"]=news_p


 # Visit nasa.gov
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(2)
     # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # BONUS: Find the src for the mars image
    relative_image_path = soup.find_all('img')[1]["src"]
    featured_image_url = url + relative_image_path
    # Store data in a dictionary
    image_data = {
        "Mars photo": featured_image_url
    }
   



    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = bs(html, "html.parser")
    hemisphere_data=[]

    relative_image_path0 = soup.find_all('img')[0]["src"]
    relative_image_path1 = soup.find_all('img')[1]["src"]
    relative_image_path2 = soup.find_all('img')[2]["src"]
    relative_image_path3 = soup.find_all('img')[3]["src"]
 
    hemisphere_data = [
        {"title": "Valles Marineris Hemisphere", "img_url": {{ relative_image_path0 }} },
        {"title": "Cerberus Hemisphere", "img_url": {{ relative_image_path1 }} },
        {"title": "Schiaparelli Hemisphere", "img_url": {{ relative_image_path2 }} },
        {"title": "Syrtis Major Hemisphere", "img_url": {{ relative_image_path3 }} }
    ]
    image_data={
      "hemisphere_image_data": hemisphere_data
    }

    # Return results
    return image_data

if __name__=="__main__":
    print(scrape_info())

