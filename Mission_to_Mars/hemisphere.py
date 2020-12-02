from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit nasa.gov
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

  

    # BONUS: Find the src for the sloth image
    relative_image_path0 = soup.find_all('img')[0]["src"]
    relative_image_path1 = soup.find_all('img')[1]["src"]
    relative_image_path2 = soup.find_all('img')[2]["src"]
    relative_image_path3 = soup.find_all('img')[3]["src"]

    #featured_image_url = url + relative_image_path

    # Store data in a dictionary
    hemisphere_image_data = [
        {"title": "Valles Marineris Hemisphere", "img_url": "relative_image_path0"},
        {"title": "Cerberus Hemisphere", "img_url": "relative_image_path1"},
        {"title": "Schiaparelli Hemisphere", "img_url": "relative_image_path2"},
        {"title": "Syrtis Major Hemisphere", "img_url": "relative_image_path3"},
    ]

    # Close the browser after scraping
    browser.quit()

    # Return results
    return hemisphere_image_data
