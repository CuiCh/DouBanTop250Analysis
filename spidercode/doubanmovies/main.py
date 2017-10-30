<<<<<<< HEAD
from scrapy import cmdline
import os

os.system('del DoubaMmovies.csv')
=======
from scrapy import cmdline
import os

os.system('del DoubaMmovies.csv')
>>>>>>> fcd31432a0445dadcfd24bf226c606dde305c838
cmdline.execute('Scrapy crawl getmoviesinfo -o DoubaMmovies.csv'.split())