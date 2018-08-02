from selenium import webdriver

url = "https://www.baidu.com"
driver_path = r"G:\tools\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
text  = driver.page_source
print(text)