import scrapy
from xkcd.items import XkcdItem

class XkcdSpider(scrapy.Spider):
	name = 'xkcd'
	allowed_domains = ['xkcd.com','imgs.xkcd.com']
	start_urls = ['https://xkcd.com/archive/']
	
	def parse(self, response):
		link = response.xpath('/html/body/div[2]/a/@href')
		for i in link:
			comic = response.urljoin(i.extract())
			yield scrapy.Request(comic, callback = self.parse_comic_page)

	def parse_comic_page(self, response):
		img_urls = []
		item = XkcdItem()
		img = response.selector.xpath('/html/body/div[2]/div[2]/img/@src').extract()
		img_url = 'https:' + img[0]
		img_urls.append(img_url)
		item['comic_name'] = response.selector.xpath('//*[@id="ctitle"]/text()').extract()[0]
		item['image_urls'] = img_urls
		yield item



	def error_response(self, failure):
		print(f'FAILURE: {failure}')