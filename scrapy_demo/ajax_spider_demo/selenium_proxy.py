from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://223.150.39.127:9000")

url = "http://httpbin.org/ip"
driver_path = r"G:\tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get(url)