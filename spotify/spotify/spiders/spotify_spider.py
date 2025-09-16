import os
from modules.file_locator import FileDirectory as fl
import scrapy
import json
import re
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "spotify"

    # 延迟初始化，避免在模块加载时就执行
    def __init__(self):
        super().__init__()
        # 文件路径
        self.file_path = fl().get_filedir("country_codes.json")
        # 国家代码列表
        self.country_codes_dict = json.load(open(self.file_path))
        # 将所有国家代码合并到一个列表中
        # 所有目标链接
        self.start_urls = []
        count = 0
        for continent, codes in self.country_codes_dict.items():
            # 遍历每个州合成链接
            for code in codes:
                url = f"https://www.spotify.com/{code}/premium/"
                self.start_urls.append(url)
                count += 1

        print("urls列表:", self.start_urls)

    def parse(self, response):
        # 获取所有Premium计划名称
        plan_names = response.css('div[style="--bottom-margin:0"] h3::text').getall()
        # 获取所有Premium计划价格
        plan_prices = []
        texts = response.css('div[style="--bottom-margin:0"] p[class^="sc-3a0437cc-6"]::text').getall()
        for text in texts:
            if text and '\xa0' in text:  # 修正这里
                text = text.replace('\xa0', ' ')
            plan_prices.append(text)

        print(f"计划名称: {plan_names} 价格: {plan_prices}")
