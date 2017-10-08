from scrapy import cmdline
import os

os.system('del DoubaMmovies.csv')
cmdline.execute('Scrapy crawl getmoviesinfo -o DoubaMmovies.csv'.split())