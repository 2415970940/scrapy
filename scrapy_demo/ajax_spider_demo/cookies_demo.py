from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://www.baidu.com"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

for cookie in driver.get_cookies():
    print(cookie)

# driver.get_cookie(key)
# driver.delete_all_cookies()
# driver.delete_cookie(key)