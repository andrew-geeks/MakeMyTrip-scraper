# Script for scraping hotel data of any given city!
# Data scraping is taking place through chromedriver(replace chromedriver.exe file if outdated). Chrome browser should be available in your system.


# -- STEPS TO FOLLOW --
# Step1: Go to https://www.makemytrip.com/hotels
# Step2: Select your desired city and checkin-checkout dates. Click Search. Then copy the URL and paste below into the MMT_LINK variable.
# Step3: Create a CSV file based on the given sample csv file (dont misplace the headers in the csv). Place its path in the CSV_PATH variable.
# Step4: Then run the script. Do not run the script in --headless mode, as it will create consequences during data extraction.

# - Some datasets have created by me(find it in hotel_datasets) for illustration purposes.
# - open an issue, if any problem arises, I will try to solve it!


import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()



options = [
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options,executable_path='chromedriver.exe')


# Add the browser url below after selecting city and dates.
# example link: https://www.makemytrip.com/hotels/hotel-listing/?checkin=08212023&city=CTCCU&checkout=08222023&roomStayQualifier=2e0e&locusId=CTCCU&country=IN&locusType=city&searchText=Kolkata&regionNearByExp=3&rsc=1e2e0e

MMT_LINK = "" 

# Add the path were the CSV file is present(below), so that the scraped data can be saved. 
# Note: First create the CSV file based on the sample dataset given before running the script, so that you wont fall into any trouble!

CSV_PATH = ""

driver.get(MMT_LINK)
time.sleep(6)
print("6 sec over")



for i in range(0,101):
    print("hotel: "+str(i))
    content = driver.find_element(By.XPATH,'//*[@id="Listing_hotel_'+str(i)+'"]')
    hname = content.find_element(By.ID,'hlistpg_hotel_name')
    print(hname.text)
    try:
        rating = content.find_element(By.ID,'hlistpg_hotel_user_rating')
        rating = rating.text
        print(rating)
        try:
            rating_desc = content.find_element(By.XPATH,'//*[@id="Listing_hotel_'+str(i)+'"]/a/div/div[1]/div[2]/div[1]/div/div/span[1]')
            rating_desc = rating_desc.text
            print(rating_desc)
        except:
            rating_desc = content.find_element(By.XPATH,'//*[@id="Listing_hotel_'+str(i)+'"]/a/div/div/div[1]/div[2]/div[2]/div/div/span[2]')
            rating_desc = rating_desc.text
            print(rating_desc.text)
        review_count = content.find_element(By.ID,'hlistpg_hotel_reviews_count')
        review_count = review_count.text
        print(review_count)
    except:
        rating=""
        rating_desc=""
        review_count=""
    
    loc = content.find_element(By.CLASS_NAME,'pc__html')
    loc = loc.text
    loc = loc.split("|")
    location = loc[0] #hotel_locationzdb
    try:
        landmark = loc[1].split('from')
        dist_landmark = landmark[0].lstrip() #distance to nearest landmark/locality
        landmark = landmark[1].lstrip() #nearest landmark/locality
    except:
        dist_landmark=""
        landmark=""

    print("location: "+location)
    print("landmark: "+landmark)
    print("dis to landmark: "+dist_landmark)
    
  
    price = content.find_element(By.ID,'hlistpg_hotel_shown_price')
    print(price.text[2:])
    
    tax = content.find_element(By.XPATH,'//*[@id="Listing_hotel_'+str(i)+'"]/a/div[1]/div/div[2]/div/div/p[2]')
    try:
        tax = tax.text.split(" ")[2]
    except:
        tax=""
    print(tax)
    
    try:
        s_rating = content.find_element(By.ID,'hlistpg_hotel_star_rating')
        s_rating = s_rating.get_attribute('data-content')
    except:
        s_rating=""
    
    print("s_rating: "+s_rating) #star_rating
    
    #csv
    data=[[hname.text,rating,rating_desc,review_count,s_rating,location,landmark,dist_landmark,price.text[2:],tax]]
    with open(CSV_PATH,'a',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(data)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.close()

