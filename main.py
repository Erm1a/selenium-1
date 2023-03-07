from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.google.com")
# a= "W0wltc"
# const1 = driver.find_element('id', a)
# const1.send_keys(Keys.ENTER)
# search = driver.find_element('name', 'q').send_keys("Selenium is fun! test 1" , Keys.ENTER)
# sleep(0.5)
# wt = driver.title
# print(wt)
# driver.get("https://www.digikala.com")
# sleep(1)
driver.refresh()
driver.switch_to.new_window("window")
driver.get("https://www.bing.com")
sleep(2)
b = driver.window_handles
driver.switch_to.window(b[0])
sleep(3)
# driver.back()
# driver.forward()
driver.quit()
