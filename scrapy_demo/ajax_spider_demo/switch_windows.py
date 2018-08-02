from selenium import webdriver

url = "https://www.douban.com"
url1 = "https://www.baidu.com"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

driver.execute_script("window.open('"+url1+"')")
print(driver.current_url)
# 虽然打开两个窗口，但是driver指向第一个，需要切换
driver.switch_to.window(driver.window_handles[2])
print(driver.current_url)