# -*- coding: utf-8 -*-
import scrapy
import re

from weiboImg.items import WeiboimgItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/u/2676540645?uid=2676540645&luicode=10000011&lfid=1008082a98366b6a3546bd16e9da0571e34b84_-_soul']

    def parse(self, response):
        print('spider')
        item = WeiboimgItem()
        imgurls = response.css("article.weibo-main > div.weibo-og > div > div.weibo-media img:not([loading]):not([data-img])::attr(src)").extract()
        for url in imgurls:
            url = re.sub('orj360', 'large', url)
            item['imgurl'] = url
            item['imgpath'] = url.split('/')[-1]
            yield item