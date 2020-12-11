from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
userID=input('Enter your email id : ')
passwd=input('Enter your password : ')
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
sleep(2)
username=driver.find_element_by_xpath('//*[@id="email"]')
password=driver.find_element_by_xpath('//*[@id="pass"]')
username.send_keys(userID)
password.send_keys(passwd)
sleep(2)
login=driver.find_element_by_xpath('//*[@id="u_0_b"]')
login.click()

