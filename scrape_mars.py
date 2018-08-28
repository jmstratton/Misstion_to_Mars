# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import pymongo
import time
import requests
import tweepy

# Define Scrape Function
def scrape():

    print("Begin Scraping")
    
# create a dictionaryt to store the data
scrape_mars_dict = {}

###  ###  NEWS  ###   ###

# Define URL
news_url = 'https://mars.nasa.gov/news/'

# Retrieve Page
html = requests.get(news_url)

# HTML Parser with Beautiful Soup
soup = BeautifulSoup(html.text, 'html.parser')

# Get article title & description
news_title = results.find('div', class_='content_title').text
news_p = soup.find('div', class_='rollover_description_inner').text

# Add to dictionary
scrape_mars_dict['news_title'] = news_title
scrape_mars_dict['newsp'] = news_p    

print("News Title & Description Retrieved")

###  ###  IMAGES  ###   ###

# Define URL
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

#Set up Splinter
executable_path = {'executable_path': '/Users/Jill Stratton/Desktop/chromedriver/chromedriver.exe'}
return Browser("chrome", **executable_path, headless=True)
browser.visit(image_url)

# Move through pages
time.sleep(5)
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(5)
browser.click_link_by_partial_text('more info')
time.sleep(5)

# HTML Parser with Beautiful Soup
image_html = browser.html
image_soup = BeautifulSoup(image_html, 'html.parser')

# Retrieve Featured Image
featured_image = image_soup.find('article')
extension = featured_image.find('figure', 'lede').a['href']
link = 'https://www.jpl.nasa.gov'
featured_image_url = link + extension

# Store url to dictionary
scrape_mars_dict['featured_image_url'] = featured_image_url

print("Featured Image Retrieved")

###  ###  MARS FACTS  ###   ###

#Define URL
facts_url = 'https://space-facts.com/mars/'

# HTML Parser with Beautiful Soup
facts_html = browser.html
facts_soup = BeautifulSoup(facts_html.text, 'html.parser')

# Create dictionary to hold info
mars_facts_dict = {}

# Get Mars Facts
facts_results = soup.find('tbody').find_all('tr')

# Store Mars Facts and Create Key
for facts_result in facts_results:
    key = facts_result.find('td', 'column-1').text.split(":")[0]
    value = facts_result.find('td', 'column-2').text
    mars_facts_dict[key] = value

# Create DataFrame
mars_facts_df = pd.DataFrame([mars_facts_dict]).T.rename(columns = {0:"Value"})
mars_facts_df.index.rename("Description", inplace = True)

# Convert to HTML
mars_facts_html = "".join(mars_facts_df.to_html().split("\n"))

# Store html file to dictionary
scrape_mars_dict['mars_facts_html'] = mars_facts_html

print("Mars Facts Retrieved")

###  ###  Hemispheres  ###   ###

# Define URL
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# Create list for images
hem_image_urls = []

###  ###  WEATHER  ###   ###

# Twitter Credentials
consumer_key = "Hg0XtmbmudwdmPb2cNCdmKmxk"
consumer_secret = "npl8cvUzLcWOceOaOLDA5TlbyoqzY838yjWg2wsCqv028MKI9m"
access_token = "3233494312-nLivXxX2PZblH51N0eDN1bHEWBYuHlrHhZ7w5sF"
access_token_secret = "GimjAoBhYuFSrIrXqfdiRUQasAhHPOcFML2Ew5oKpwI8a"

# Use Tweepy to Authenticate Access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = "@MarsWxReport"

# Get Tweets
tweet = api.user_timeline(target_user, count=1)[0]

# Store Weather Results
mars_weather = tweet['text']

# Add to dictionary
scrape_mars_dict["mars_weather"] = mars_weather

print ("Mars Weather Retrieved")


## ## ## First Hemisphere - Valles Marineris ## ## ##
# Set up Splinter
executable_path = {'executable_path': '/Users/Jill Stratton/Desktop/chromedriver/chromedriver.exe'}
return Browser("chrome", **executable_path, headless=True)
browser.visit(hemisphere_url)

# Move through pages
time.sleep(5)
browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
time.sleep(5)

# HTML Parser with Beautiful Soup
hem1_html = browser.html
hem1_soup = BeautifulSoup(hem1_html, 'html.parser')

# Save the link
hem1_link = hem1_soup.find('div', 'downloads').a['href']

# Create dictionary for image
valles_marineris = {
    "title": "Valles Marineris Hemisphere",
    "img_url": hem1_link
}

# Append dictionary with results
hem_image_urls.append(valles_marineris)

## ## ## Second Hemisphere - Cerberus  ## ## ##
# Set up Splinter
executable_path = {'executable_path': '/Users/Jill Stratton/Desktop/chromedriver/chromedriver.exe'}
return Browser("chrome", **executable_path, headless=True)
browser.visit(hemisphere_url)

# Move through pages
time.sleep(5)
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
time.sleep(5)

# HTML Parser with Beautiful Soup
hem2_html = browser.html
hem2_soup = BeautifulSoup(hem2_html, 'html.parser')

# Save the link
hem2_link = hem2_soup.find('div', 'downloads').a['href']

# Create dictionary for image
cerberus = {
    "title": "Cerberus Hemisphere",
    "img_url": hem2_link
}

# Append dictionary with results
hem_image_urls.append(cerberus)

## ## ## Third Hemisphere - Schiaparelli ## ## ##
# Set up Splinter
executable_path = {'executable_path': '/Users/Jill Stratton/Desktop/chromedriver/chromedriver.exe'}
return Browser("chrome", **executable_path, headless=True)
browser.visit(hemisphere_url)

# Move through pages
time.sleep(5)
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
time.sleep(5)

# HTML Parser with Beautiful Soup
hem3_html = browser.html
hem3_soup = BeautifulSoup(hem3_html, 'html.parser')

# Save the link
hem3_link = hem3_soup.find('div', 'downloads').a['href']

# Create dictionary for image
schiaparelli = {
    "title": "Schiaparelli Hemisphere",
    "img_url": hem3_link
}

# Append dictionary with results
hem_image_urls.append(Schiaparelli)

## ## ## Fourth Hemisphere - Syrtis Major ## ## ##
# Set up Splinter
executable_path = {'executable_path': '/Users/Jill Stratton/Desktop/chromedriver/chromedriver.exe'}
return Browser("chrome", **executable_path, headless=True)
browser.visit(hemisphere_url)

# Move through pages
time.sleep(5)
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
time.sleep(5)

# HTML Parser with Beautiful Soup
hem4_html = browser.html
hem4_soup = BeautifulSoup(hem4_html, 'html.parser')

# Save the link
hem4_link = hem4_soup.find('div', 'downloads').a['href']

# Create dictionary for image
syrtis_major = {
    "title": "Syrtis Major Hemisphere",
    "img_url": hem4_link
}

# Append dictionary with results
hem_image_urls.append(syrtis_major)

# Add to Dictionary
scrape_mars_dict[hem_image_urls] = hem_image_urls

print("Hemisphere Pictures Retrieved")
print("#########################################################")
print("End Scraping")

return scrape_mars_dict