from bs4 import BeautifulSoup as bs
from splinter import Browser
#import requests
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path':'C:/Users/Bowen Prince/Desktop/web-scraping-challenge/mission to mars/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

#url1
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)
    html = browser.html

    #response = requests.get(url)
    soup1 = bs(html, 'html.parser')

    latest_title = []
    latest_paragraph = []

    title = soup1.find('div', class_= 'content_title').text.strip()
    paragraphs = soup1.find('div', class_='rollover_description_inner').text.strip()


    latest_title.append(title)
    latest_paragraph.append(paragraphs)



#url2
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    time.sleep(1)
    html = browser.html

    #response2 = requests.get(url2)
    soup2= bs(html, 'html.parser')
    results2 = soup2.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()
    href=results2
    featured_img = (url2 + href)

#url3
#     url3 = "https://twitter.com/marswxreport?lang=en"
#     browser.visit(url3)
#     #response3 = requests.get(url3)
#     html = browser.html
#     soup3 = bs(html, "html.parser")


#     #results3 = soup3.find("p", class_="TweetTextSize")[0].text
#    # results3 = soup3.find_next("p", class_="tweet-text")[0].get_text()
#     #results3 = soup3.find_next("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").get_text()
#     latest_tweet = results3


#url4
    url4 = "https://space-facts.com/mars/"
    table = pd.read_html(url4)
    df = table[0]
    df.columns = ["Prompt", "Fact"]
    df.reset_index(drop=True, inplace=True)

    comparison = table[1]
    comparison.set_index("Mars - Earth Comparison")

    html_table_1 = df.to_html()
    html_table_2 = comparison.to_html()
    html_table_1

    final_table1 = html_table_1.replace('\n', '')
    final_table2 = html_table_2.replace('\n', '')


#url5, url6, url7, url8
    url5 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"

    #response5 = requests.get(url5)
    browser.visit(url5)
    html = browser.html
    soup5 = bs(html, 'html.parser')
    results5 = soup5.find("h2", class_="title").text 
    
    url6 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    url7 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    url8 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

    #response6 = requests.get(url6)
    browser.visit(url6)
    html = browser.html
    soup6 = bs(html, 'html.parser')
    results6 = soup6.find("h2", class_="title").text 

    url7 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"

    #response7 = requests.get(url7)
    browser.visit(url7)
    html = browser.html
    soup7 = bs(html, 'html.parser')
    results7 = soup7.find("h2", class_="title").text
    
    url8 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

    #response8 = requests.get(url8)
    browser.visit(url8)
    html = browser.html
    soup8 = bs(html, 'html.parser')
    results8 = soup8.find("h2", class_="title").text 


    img5 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
    img6 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"
    img7 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"
    img8 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"



    hemisphere_image_urls = [
        {"title": results5, "img_url": img5},
        {"title": results6, "img_url": img6},
        {"title": results7, "img_url": img7},
        {"title": results8, "img_url": img8},
    ]


    hemisphere_image_urls


    mars_data = {"Latest Title": latest_title, "Latest Paragraph": latest_paragraph, "Featured Image": featured_img, "Table 1": final_table1, "Table 2": final_table2, "Hemisphere Images": hemisphere_image_urls}
#"Latest Tweet": latest_tweet
    return mars_data
