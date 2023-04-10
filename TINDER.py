import time
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# creating webdriver object to perform rest of operations on it ************************************************************************************

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("HTTPS://TINDER.COM")
sleep(randint(1, 2))


# Dealing small pop ups on page before login *******************************************************************************************************

# Accept cookies
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]").click()
except:
    sleep(randint(1, 2))

#login button click
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]").click()
sleep(randint(1, 2))

# Trying facebook login and create a window handle before login ****************************************************************************************


try:                
    old_window = driver.window_handles[0]
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div").click()

except:           #more options and then facebook
    
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/button").click()
    old_window = driver.window_handles[0]
    driver.find_element(By.XPATH,
                        "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div").click()
sleep(randint(1, 2))



# creating a window handle for new facebook window and switching to it to perform operations****************************************************

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)                        
sleep(randint(1, 2))


# entering username and password ***************************************************************************************************************

user_name = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input").send_keys("     ")
sleep(randint(1, 2))
password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input").send_keys("     ")
#submit login
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input").click()
sleep(randint(5, 7))

# switching back to old handle ************************************************************************************************************


#switching back
driver.switch_to.window(old_window)
sleep(randint(1, 2))


# we are logged in at this moment ******************************************************************************************************************************


# allow location
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]").click()
    sleep(randint(1, 2))
except:
    sleep(randint(1, 2))
    
    
#allow notification
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]").click()
    sleep(randint(1, 2))
except:
    sleep(randint(1, 2))
sleep(randint(5, 8))


# It's swiping time *********************************************************************************************************************************************
i = 0
while i < 100:
    try:
        driver.find_element(By.XPATH, '//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT)
        sleep(randint(1, 2))
        i = i + 1
    except:
        driver.refresh()
        time.sleep(3)






