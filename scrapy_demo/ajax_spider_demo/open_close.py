from selenium import webdriver
import time

url = "https://www.baidu.com"
# driver_path = r"D:\Python\Python35\chromedriver.exe"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,service_args = ['--ignore-ssl-errors=true'])
driver.get(url)

time.sleep(3)

driver.close()
# driver.quit()
