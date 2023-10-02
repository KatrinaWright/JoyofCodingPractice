#Youtube Scraper and Meeting Summary maker
#Katrina Wright - Joy of Coding Academy
#Used tutorial from brightdata: https://brightdata.com/blog/how-tos/how-to-scrape-youtube-in-python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options      ##UNCOMMENT WHEN WANTING HEADLESS TO BE ACTIVATED
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
import json

# initialize a web driver instance to control a Chrome window in headless mode
#options = Options()
#options.add_argument('--headless=new')

def consent_cookies_clicker():
    try: 

        # wait up to 15 seconds for the consent dialog to show up
        consent_overlay = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'dialog'))
        )

        # select the consent option buttons
        consent_buttons = consent_overlay.find_elements(By.CSS_SELECTOR, '.eom-buttons button.yt-spec-button-shape-next')
        if len(consent_buttons) > 1:
            # retrieve and click the 'Accept all' button
            accept_all_button = consent_buttons[1]
            accept_all_button.click()
    except TimeoutException:
        print('Cookie modal missing')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())#, 
    #options=options
    )

##########################################
#scraping logic below ....

# The URL of the target page
url1 = 'https://youtu.be/76RHck_RCB8?feature=shared'


def scrape_YTVideo(url, cookies=False):
    #visit the target page in the controlled browser
    driver.get(url)

    if cookies == True:
        consent_cookies_clicker()                           # Use only if cookies modal needs to be accepted

    #Wait for YouTube to load the page data
    WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'h1.ytd-watch-metadata'))
    )
    print("I see it! I'm here:   ", url)

    video = {}

    title = driver.find_element(By.CSS_SELECTOR, 'h1.ytd-watch-metadata').text
    print("Heres the title:      ", title)

    video['url'] = url
    video['title'] = title

    print('Heres the dictionary: ', video)

    with open('video.json', 'w') as file:
        json.dump(video, file, indent=4)


    # close the browser and free up the resources
    driver.quit()

def main():
    scrape_YTVideo(url1)

main()