import scrapy


class SaiteichinginSpider(scrapy.Spider):
    name = 'saiteichingin'
    start_urls = ['https://pc.saiteichingin.info/table/page_list_nationallist.php']

    def parse(self, response):
        regions = response.css('.list::text').getall() # len 10
        prefectures = response.css('#maincont td:nth-child(1) ::text').getall() # len 47
        money = response.css('.money::text').getall() #len 47
        date = response.css('.date::text').getall() # len 47
        for pos in range(len(prefectures)):
            yield {
                'prefectures': prefectures[pos],
                'money': money[pos],
                'date': date[pos]
            }
        pass
