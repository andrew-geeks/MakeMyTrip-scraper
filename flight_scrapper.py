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
    "--disable-dev-shm-usage",
    "--disable-blink-features",
    "--disable-blink-features=AutomationControlled",
    "--disable-3d-apis"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options,executable_path='chromedriver.exe')

driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary=HYD-DEL-31/08/2023&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1693316463663&forwardFlowRequired=true&mpo=&semType=&intl=false")
time.sleep(25)

CSV_PATH = "flight_datasets/flight_data_DEL_HYD.csv"

COUNT = 50

for i in range(1,COUNT+1):
        try:
            block = driver.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']')
        except:
            driver.close() #page closes when scraping is over
        try:
            #scrapecode
            driver.find_element(By.XPATH, '//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[3]/span').click()
            time.sleep(1)
            fname = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[1]/div/p[1]').text
            print(fname)
            fcode = block.find_element(By.CLASS_NAME,'fliCode').text
            print("flightcode: "+fcode)
            
            #DEPARTURE
            deptime = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[1]/p[1]').text 
            print("deptime: "+deptime)
            depcity = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[1]/p[2]').text
            print("depcity: "+depcity)
    
            #ARRIVAL
            arrtime = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[3]/p[1]').text
            print("arrtime: "+arrtime)
            arrcity = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[3]/p[2]').text
            print("arrcity:"+arrcity)
            duration = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[2]/p').text
            print("duration: "+duration)
            
            price = driver.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[2]/div/div/div').text
            price = price.split('\n')
            price = price[0][2:]
            print("price: "+price)
            
            
            
        except:
            pass
        data=[[fname,fcode,depcity,deptime,arrcity,arrtime,duration,price]]
        with open(CSV_PATH,'a',newline='',encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerows(data)
        time.sleep(2)
        
   

driver.close()

#