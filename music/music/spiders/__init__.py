# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class MusicScraping(scrapy.Spider):
    name = 'music'



    def start_requests(self):
        yield scrapy.Request('https://www.last.fm/music/+coming-soon', callback=self.parse_music)


    def parse_music(self , response):
        for music in response.css('#mantle_skin > div.container.page-content > div > div.col-main > ol>li'):
            yield {
                'title': music.css('div > h3 > a::text').extract_first(),
                'author': music.css('div > p.album-grid-item-artist > span > a::text').extract_first(),
                'image': music.css('div > img::attr(src)').extract_first(),
                'tags': music.css('div > ul > li > a::text').extract()
            }
        next_page = response.css('.pagination > .next > a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_music)
