from ptt.items import PostItem
import scrapy
import time

class PTTSpider(scrapy.Spider):    # 繼承 scrapy.Spider , 除了 parse_article, 其他在父類別都有事先定義
    name = 'ptt'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']


    def parse(self, response):
        for i in range(100):
            time.sleep(1)
            url = "https://www.ptt.cc/bbs/Gossiping/index" + str(100 - i) + ".html"
            yield scrapy.Request (url, cookies={'over18': '1'}, callback=self.parse_article)
    
    
    def parse_article(self, response):
        item = PostItem()
        target = response.css("div.r-ent")
    
    
        for tag in target:
            try:
                item['title'] = tag.css("div.title a::text")[0].extract()
                item['author'] = tag.css('div.author::text')[0].extract()
                item['date'] = tag.css('div.date::text')[0].extract()
                item['push'] = tag.css('span::text')[0].extract()
                item['url'] = tag.css('div.title a::attr(href)')[0].extract()
    
                yield item
    
            except IndexError:
                pass
            continue
