# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from xkcd.items import XkcdItem

class XkcdPipeline:

	name = ''

    def process_item(self, item, spider):
        self.name = item['comic_name']

   	def file_path():
   		return self.name
