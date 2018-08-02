from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://www.baidu.com"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,"python")
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()

# actions.click_and_hold() 点击不松开鼠标
# actions.context_click()  右键点击
# actions.double_click()  双击