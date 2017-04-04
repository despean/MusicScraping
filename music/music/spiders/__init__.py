# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class MusicScraping(scrapy.Spider):
    name = 'music'
    start_urls =[
        'https://www.last.fm/music/+coming-soon'
    ]
    def parse(self , response):
        for music in response.css('#mantle_skin > div.container.page-content > div > div.col-main > ol>li'):
            yield {
                'title': music.css('div > h3 > a::text').extract_first(),
                'author': music.css('div > p.album-grid-item-artist > span > a::text').extract_first(),
                'image': music.css('div > img::attr(src)').extract_first(),
                'tags': music.css('div > ul > li > a::text').extract()
            }

