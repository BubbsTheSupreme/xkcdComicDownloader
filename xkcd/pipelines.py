# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from xkcd.items import XkcdItem

class XkcdPipeline(ImagesPipeline):

	def file_path(self, request, response=None, info=None):
		return request.url.split('/')[-1]