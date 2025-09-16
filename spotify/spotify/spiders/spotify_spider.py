import os
from modules.file_locator import FileDirectory as fl

import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "spotify"

    # 延迟初始化，避免在模块加载时就执行
    def __init__(self):
        super().__init__()
        self.file_path = fl().get_filedir("country_codes.json")
        self.country_codes_dict = json.load(open(self.file_path))
        # 将所有国家代码合并到一个列表中
        # self.country_codes = [code for region_codes in self.country_codes_dict.values() for code in region_codes]
        self.start_urls = []
        count = 0
        for region, region_codes in self.country_codes_dict.items():
            print("正在爬取区域: {region_codes}")
            for code in region_codes:
                url = f"https://www.spotify.com/{code}/premium/"
                self.start_urls.append(url)
                count += 1
                print(f"第 {count} 个国家代码: {code}")
        print("url列表:", self.start_urls)
    def parse(self, response):
        # print("文件根目录为:", self.file_path)
        # print("国家代码列表为:", self.country_codes)

        # 获取Premium计划名称
        plan_name = response.css('div [id*=plan-premium] div h3::text').get()
        # 获取Premium计划价格
        plan_price = response.css('div [id*=plan-premium] div p::text').get()


        print("计划名为:", plan_name)
        print("计划名为:", plan_price)