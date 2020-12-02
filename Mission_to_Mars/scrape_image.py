
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
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

  

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[1]["src"]
    featured_image_url = url + relative_image_path

    # Store data in a dictionary
    image_data = {
        "Mars photo": featured_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return image_data
