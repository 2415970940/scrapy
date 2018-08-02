from selenium import webdriver

url = "https://www.douban.com"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

# 隐式等待
# driver.implicitly_wait(10)
# driver.find_element_by_id('form_email')

# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

element = WebDriverWait(driver,10).until(expected_conditions.presence_of_all_elements_located((By.ID,'form_email')))
print(element)