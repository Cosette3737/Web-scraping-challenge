
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
    mars_data={}

#grab title and text
    url ='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
   
    news_title= soup.find_all('div', class_='content_title')
    news_title= news_title[1].a.text
    
    news_p = soup.find_all('div', class_='article_teaser_body')
    news_p = news_p[0].text
   
    #Add title and text to image data
    mars_data["news_title"]=news_title
    mars_data["news_p"]=news_p


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
    mars_data = {
        "Mars photo": featured_image_url
    }
   


    url= 'https://space-facts.com/mars/'
    table= pd.read_html(url)
    table[0]
    df= table[0]
    df.columns= ["Description", "Values"]
    df.set_index("Description", inplace= True)
    df
    html_table= df.to_html()
    html_table= html_table.replace('\n', '')
    mars_data["results_table"]= html_table
    
    
    
    
    
    
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    hemisphere_data=[]

    for x in range(4):
        hemisphere={}
        time.sleep(2)
        browser.find_by_css("a.product-item h3")[x].click()
        soup=bs(browser.html, 'html.parser')
        title=soup.find("h2", class_="title").get_text()
        image=soup.find("a",text="Sample").get("href")
        hemisphere["img_url"]=image
        hemisphere["title"]=title
        hemisphere_data.append(hemisphere)
        browser.back()

    mars_data["hemisphere"]=hemisphere_data



    # Return results

    mars_data={
        "news_title":news_title,
        "news_p":news_p,
        "Mars photo": featured_image_url,
        "results_table": html_table,
        "hemisphere_image_title_1": hemisphere_data[0]["title"],
        "hemisphere_image_url_1": hemisphere_data[0]["img_url"],
        "hemisphere_image_title_2": hemisphere_data[1]["title"],
        "hemisphere_image_url_2": hemisphere_data[1]["img_url"],
        "hemisphere_image_title_3": hemisphere_data[2]["title"],
        "hemisphere_image_url_3": hemisphere_data[2]["img_url"],
        "hemisphere_image_title_4": hemisphere_data[3]["title"],
        "hemisphere_image_url_4": hemisphere_data[3]["img_url"]
    }
  
    return mars_data

if __name__== "__main__":
    print(scrape_info())

