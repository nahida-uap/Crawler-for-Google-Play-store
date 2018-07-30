import time
import csv
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# @author Nahida Sultana Chowdhury <nschowdh@iu.edu>
#additionally add CSV file method here...

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
chromedriver_loc = "/home/mitu/Desktop/gcrawlertest/my_crawler/env/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_loc)
wait = WebDriverWait( driver, 10 )

# Append your app store urls here
urls = ["https://play.google.com/store/apps/details?id=com.facebook.orca"
]
appCounter = 0
for url in urls:
    #print(url)
    time.sleep(1)
    try:
        driver.get(url)
        driver.maximize_window()
        
        appCounter = appCounter + 1
        page = driver.page_source
        
        soup_expatistan = BeautifulSoup(page, "html.parser")
        expatistan_table = soup_expatistan.find("h1", class_="AHFaub")
        print("App name: ", expatistan_table.string)
        
        try:
            read_all_reviews_button = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div/div[6]/div/content')

            read_all_reviews_button.click()
        
            actions = ActionChains(driver)
            for _ in range(15):
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(1)
            try:
                show_more_button = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div/content')
                for i in range(0,5):
                    try:
                        show_more_button.click()
                        for _ in range(5):   #Adjust this range according to your need, I mean how far you wanna go down.
                            actions.send_keys(Keys.SPACE).perform()
                            time.sleep(1)
                    except Exception:
                        time.sleep(1)
            except Exception:
                time.sleep(1)

            reviews_div = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div').get_attribute("innerHTML")

            soup_expatistan = BeautifulSoup(reviews_div, "html.parser")

            expand_pages = soup_expatistan.find_all("div", class_="d15Mdf bAhLNe")
        
            try:
                myFile = open('/home/mitu/Desktop/gcrawlertest/my_crawler/env/bin/test/'+str(appCounter)+'_rev.csv',"w")
                with myFile:
                    writer = csv.writer(myFile)
                    for expand_page in expand_pages:
                        ind_rev = expand_page.find("span", class_="p2TkOb")
                        ind_rev_date = expand_page.find("div", class_="UD7Dzf")
                        
                        num_of_star = 0
                        star_count = expand_page.find_all("div", class_="vQHuPe bUWb7c")    
                        for star in star_count:
                            num_of_star = num_of_star + 1
                        #print(num_of_star)
                        
                        csvRow = [num_of_star, ind_rev.text.encode("utf8"), ind_rev_date.text.encode("utf8")]
                        writer.writerow(csvRow)
                myFile.close()
            except Exception:
                print("file open error")
        except Exception:
            time.sleep(1)
    except Exception:
            time.sleep(1)
driver.quit()
