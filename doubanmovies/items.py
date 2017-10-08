# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class DoubanmoviesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = Field()
    OriginalTitle = Field()
    Year = Field()
    Rank = Field()
    Direction = Field()
    ScreenWriter = Field()
    Actors = Field()
    MovieTypes = Field()
    CountryOrRegion = Field()
    Last = Field()
    Votes = Field()
    Score = Field()
    Comment = Field()
    Url = Field()
