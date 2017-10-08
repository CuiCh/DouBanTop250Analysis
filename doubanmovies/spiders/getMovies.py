from scrapy import Spider
import scrapy
from doubanmovies.items import DoubanmoviesItem
from scrapy.selector import Selector
from scrapy.http import Request


class getmoviespider(Spider):

    name = 'getmoviesinfo'
    start_urls = ['https://movie.douban.com/top250']

    def parseSinglePage(self, response):
        item = response.meta['item']
        sel = Selector(response)

        titleinfo = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        title = titleinfo.split()[0]
        originalTitle = titleinfo.split()[1:]

        year = sel.xpath('//*[@id="content"]/h1/span[2]/text()').extract_first()
        direction = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        screenwriter = sel.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        actors = sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()

        movietype = sel.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
        last = sel.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content').extract_first()
        audience = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract_first()
        countryorregion = sel.xpath('//*[@id="info"]/span[@class="pl"][2]/following-sibling::text()').extract_first().strip().split('/')

        item['Title'] = title
        item['OriginalTitle'] = ' '.join(originalTitle)
        item['Year'] = year[1:-1]
        item['Direction'] = ' '.join(direction)
        item['Actors'] = ' '.join(actors)
        item['ScreenWriter'] = ' '.join(screenwriter)
        item['MovieTypes'] = " ".join(movietype)
        item['Last'] = last
        item['Votes'] = audience
        item['CountryOrRegion'] = ' '.join(countryorregion)

        yield item

    def parse(self, response):
        
        sel = Selector(response)
        movielist = sel.xpath('//*[@id="content"]/div/div[1]/ol/li')

        next_link = sel.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if next_link:
            next_link = "https://movie.douban.com/top250" + next_link
            print(next_link)
            yield Request(next_link, callback=self.parse)

        for movie in movielist:
            item = DoubanmoviesItem()
            # @表示提取某一属性
            url = movie.xpath('div/div[2]/div[1]/a/@href').extract()[0]
            rank = movie.xpath('div/div[1]/em/text()').extract()[0]
            score = movie.xpath('div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            comment = movie.xpath('div/div[2]/div[2]/p[2]/span/text()').extract()[0]
            item['Url'] = url
            item['Rank'] = rank
            item['Score'] = score
            item['Comment'] = comment
            request = Request(url, callback=self.parseSinglePage, meta={'item': item})
            # request.meta['item'] = item
            yield request




