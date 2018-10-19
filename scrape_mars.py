
# coding: utf-8

# In[52]:


# Import Dependencies
import os
import pandas as pd
import numpy as np
import pymongo

# In[53]:


from bs4 import BeautifulSoup
import requests
import time


# In[54]:


from splinter import Browser
from selenium import webdriver


# Scrapping

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
# In[55]:
def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}
    urls = []
    # Latest news
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)




# In[56]:


#retrieve page with the request module
response = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[57]:


nasa_news_title = soup.find ("div", class_= "content_title").text
nasa_news_paragraph = soup.find ("div" , class_= "rollover_description_inner").text
print(nasa_news_title)
print(nasa_news_paragraph) 


# JPL MARS SPACE IMAGES

# In[58]:


#setting up splinter path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
browser.visit(url)


# In[59]:


#URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url) 


# In[60]:


mars_images = requests.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
mars_soup = BeautifulSoup(mars_images.content, 'html.parser') 


# In[61]:


image = mars_soup .find('div', class_='carousel_items')
image_url = image.article['style']
url=image_url.split('/',1)[1].split("'",1)[0]
featured_image_url= 'https://www.jpl.nasa.gov' + '/' + url 
print(featured_image_url )


# In[62]:


mars_featured_image = "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA17843-1920x1200.jpg" 


# MARS WEATHER

# In[63]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[64]:


#scrape Mars Weather Twitter Account and scrape latest Mars weather tweet
weather_url= 'https://twitter.com/MarsWxReport/status/1041843517113475075'


# In[65]:


weather_response = requests.get(weather_url)
weather_soup = BeautifulSoup(weather_response.text, 'html.parser')


# In[66]:


print(weather_soup.prettify())


# In[67]:


mars_weather = weather_soup.find('title').get_text()
mars_weather = mars_weather.split('"')[1]
#mars_weather = weather_request.find('p', class_="tweet-text").text
print(mars_weather)


#is_night = weather["temp"].str.contains("Low")


# MARS FACTS

# In[68]:


#Mars Facts
mars_facts = requests.get('https://space-facts.com/mars/')
facts_soup = pd.read_html('https://space-facts.com/mars/', header=0)
for facts in facts_soup:
    print(facts_soup)


# In[69]:


df_mars_facts = facts_soup[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[70]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# In[71]:


df_mars_facts.to_html('table.html')
get_ipython().system(' open table.html ')


# MARS HEMISPHERE

# In[72]:


#setting up splinter path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


hemi_image_urls = []
browser = Browser('chrome', headless=False)
hemi_urls = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
                   'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                   'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
                   'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
for url in hemi_urls:
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    hemi_soup = BeautifulSoup(html, 'html.parser')

    dictionary = {}
    hemi_title = hemi_soup.find('div', class_='content')
    dictionary["title"] = hemi_title.h2.text.lstrip()
    
    hemi_download=hemi_soup.find('div', class_='downloads')
    image=hemi_download.find('li')
    dictionary["image_url"] = image.find('a')['href']
    print(dictionary)
    hemi_image_urls.append(dictionary)
{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}
{'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}
{'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}
{'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}


# In[ ]:


hemi_image_urls[0]


# In[ ]:


# Convert this jupyter notebook file to a python script called 'scrape_mars.py'
get_ipython().system(' jupyter nbconvert --to script --template basic mission_to_mars.ipynb --output scrape_mars')

