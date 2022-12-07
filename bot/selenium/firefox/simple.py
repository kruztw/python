from shutil import which
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driverPath = which('geckodriver')
if driverPath == None:
    print("geckodriver not found")
    exit(0)

wd = webdriver.Firefox(service_log_path='./my.log')
wd.get("http://localhost:5000")

account_xpath = '//input[@name="username"]'
WebDriverWait(wd, timeout=60, poll_frequency=1).until(lambda driver: driver.find_element(By.XPATH, account_xpath))
target = wd.find_element(By.XPATH, account_xpath)

target.send_keys("my_account")

# password as well

button_xpath = '//button[@type="submit"]'
target = wd.find_element(By.XPATH, button_xpath)
ActionChains(wd).click(target).perform()

sleep(3)
wd.close()