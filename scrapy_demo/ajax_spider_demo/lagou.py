from selenium import webdriver
from lxml import etree
import re

class LagouSpider(object):
    driver_path = r"G:\tools\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?px=default&city=%E8%A5%BF%E5%AE%89#filterBox"
        self.positions = []


    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        self.parse_list_page(source)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            break

    def request_detail_page(self,url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job = html.xpath("//dd[@class='job_request']//span")
        salary = job[0].xpath(".//text()")[0]
        city = job[1].xpath(".//text()")[0]
        city = re.sub(r"[\s/]","",city)
        work_year=job[2].xpath(".//text()")[0]
        work_year = re.sub(r"[\s/]","",work_year)
        edutation=job[3].xpath(".//text()")[0]
        edutation = re.sub(r"[\s/]","",edutation)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        print(desc)
        position = {
            "name":position_name,
            "salary":salary,
            "city":city,
            "work_years":work_year,
            "education":edutation,
            "description":desc
        }
        self.positions.append(position)




if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
    # print(spider.positions)
