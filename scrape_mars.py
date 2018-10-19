
# coding: utf-8

# In[34]:


# Import Dependencies
import os
import pandas as pd
import numpy as np


# In[35]:


from bs4 import BeautifulSoup
import requests
import time


# Scrapping

# In[36]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


# In[37]:


#retrieve page with the request module
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[38]:


nasa_news_title = soup.find ("div", class_= "content_title").text
nasa_news_paragraph = soup.find ("div" , class_= "rollover_description_inner").text
print(nasa_news_title)
print(nasa_news_paragraph) 


# JPL MARS SPACE IMAGES

# In[39]:


from splinter import Browser
from selenium import webdriver


# In[40]:


#setting up splinter path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
browser.visit(url)


# In[41]:


#URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url) 


# In[42]:


mars_images = requests.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
mars_soup = BeautifulSoup(mars_images.content, 'html.parser')


# In[43]:


for link in mars_soup.find('div', class_='img'):
    print(link)


# In[44]:


mars_featured_image = "/spaceimages/images/wallpaper/PIA22807-640x350.jpg"


# MARS WEATHER

# In[45]:


from splinter import Browser


# In[46]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[47]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')
weather = weather_soup.find('div', class_='js-tweet-text-container')
mars_weather= weather.p.text.lstrip()


# In[48]:


print(mars_weather)


# MARS FACTS

# In[49]:


#Mars Facts
mars_facts = requests.get('https://space-facts.com/mars/')
facts_soup = pd.read_html('https://space-facts.com/mars/', header=0)
for facts in facts_soup:
    print(facts_soup)


# In[50]:


df_mars_facts = facts_soup[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[51]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# MARS HEMISPHERE

# In[54]:


#setting up splinter path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[55]:


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


# In[56]:


hemi_image_urls[0]


# In[57]:
