from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service= Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.google.com")
# a= "W0wltc"
# const1 = driver.find_element('id', a)
# const1.send_keys(Keys.ENTER)

search = driver.find_element('name', 'q')
search.send_keys("Selenium is fun! test 1")
search.send_keys(Keys.ENTER)

