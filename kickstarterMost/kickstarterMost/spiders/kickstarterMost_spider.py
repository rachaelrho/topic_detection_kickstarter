import scrapy
import urlparse

from kickstarterMost.items import KickstarterMostItem

class kickstarterMost_spider(scrapy.Spider):
    name = "kickstarterMost"
    allowed_domains = ["kickstarter.com"]
    start_urls = ["https://www.kickstarter.com/discover/advanced?recommended=false&sort=most_funded&seed=2439769&page=" + str(x) for x in range(1,201)] 

    def parse(self, response):
        for href in response.xpath("//div[contains(concat(' ',normalize-space(@class),' '),' project-profile-title ')]/a//@href"):
            #if "most_funded" in href.extract():
            url = urlparse.urljoin("http://www.kickstarter.com",href.extract())[:-16] + str('/description')
            #else:
            #url = urlparse.urljoin("http://wwww.kickstarter.com",href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        item = KickstarterMostItem()
        item['url'] = response.url
        item['cat'] = response.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[2]/text()').extract()
        item['title'] = response.xpath('//*[@id="content-wrap"]/section/div[2]/div[1]/h2/span/a/text()').extract()
        item['blurb'] = response.xpath('//*[@id="content-wrap"]/section/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/span/span/text()').extract()
        item['desc'] = response.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]//text()').extract()
        item['rewards'] = response.xpath("//div[contains(concat(' ',normalize-space(@class),' '),' pledge__reward-description pledge__reward-description--expanded ')]//text()").extract()
        yield item

