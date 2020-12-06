#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
import os
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


# In[2]:

def scrape_info():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_data= {}


# In[3]:


    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[4]:


    response=requests.get(url)


# In[5]:


    soup = BeautifulSoup(response.text,'html.parser')


# In[6]:


    print(soup.prettify())


# In[7]:


    results=soup.find_all('div', class_="features")
    print(results)


# In[8]:


    for result in results:
        news_title = result.find('div', class_="content_title").text
        news_p = result.find('div', class_="rollover_description_inner").text


# In[9]:


    mars_data["news_title"]=news_title
    mars_data["news_p"]=news_p
    browser.quit


# In[10]:


    soup


# In[12]:


    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.find_link_by_partial_text("more info").click()
    time.sleep(2)
    soup=BeautifulSoup(browser.html,'html.parser')
    result=soup.find("figure", class_="lede")
    result=result.a.img["src"]
    result
    featured_image_url="https://www.jpl.nasa.gov" + result


# In[13]:


    print(featured_image_url)
    mars_data["featured_image_url"]=featured_image_url


# In[14]:


    import pandas as pd 
    url ='https://space-facts.com/mars'


# In[15]:


    tables=pd.read_html(url)
    tables[0]
    marstable=tables[0]


# In[16]:


    from IPython.display import HTML


# In[17]:


    result = marstable.to_html()
    print(result)
    mars_data["results_table"]=result


# In[ ]:


    mars_data


# In[18]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    hemisphere_data= []

    for x in range (4):
        hemispheres= {}
        time.sleep(2)
        browser.find_by_css("a.product-item h3")[x].click()
        soup= BeautifulSoup(browser.html, 'html.parser')
        title= soup.find("h2", class_= "title").get_text()
        image= soup.find("a", text= "Sample").get("href")
        hemispheres["title"]= title
        hemispheres["img_url"]= image
        hemisphere_data.append(hemispheres)
        browser.back()
    
    mars_data["hemispheres"]= hemisphere_data


# In[19]:


    mars_data["hemispheres"]


# In[20]:


    return mars_data

if __name__ == "__main__":
    print(scrape_info())

# In[ ]:




# In[ ]:




