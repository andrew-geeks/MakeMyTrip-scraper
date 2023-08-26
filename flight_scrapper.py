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

driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary=DEL-BOM-28/08/2023&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1693071309389&forwardFlowRequired=true&mpo=&semType=&intl=false")
time.sleep(25)

COUNT = 50

for i in range(1,COUNT+1):
    
        block = driver.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']')
        
        try:
            #scrapecode
            driver.find_element(By.XPATH, '//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[3]/span').click()
            time.sleep(1)
            fname = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[1]/div/p[1]').text
            print(fname)
            
            #DEPARTURE
            deptime = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[1]/p[1]').text 
            print("deptime: "+deptime)
            depcity = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[1]/p[2]').text
            print("depcity: "+depcity)
            depterminal = block.find_element(By.XPATH,'//*[@id="flightDetailsTab-'+str(i-1)+'-tabpane-1"]/div/div/div/div/div/div[1]/div[1]/font').text
            print("depterminal: "+depterminal)
            #ARRIVAL
            arrtime = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[3]/p[1]').text
            print("arrtime: "+arrtime)
            arrcity = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[3]/p[2]').text
            print("arrcity:"+arrcity)
            duration = block.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[1]/div[3]/label/div/div/div/div[2]/p').text
            print("duration: "+duration)
            
            price = driver.find_element(By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div['+str(i)+']/div[1]/div[2]/div[2]/div/div/div').text
            price = price.split('\n')
            price = price[0]
            print("price: "+price)
            
        except:
            pass
        time.sleep(2)
        
   

driver.close()
    
    


# //*[@id="flightDetailsTab-1-tabpane-1"]/div/div/div/div/div/div[1]/div[1]/font
#  //*[@id="flightDetailsTab-0-tabpane-1"]/div/div/div/div/div/div[1]/div[1]/font
#  //*[@id="flightDetailsTab-2-tabpane-1"]/div/div/div/div/div/div[1]/div[1]/font