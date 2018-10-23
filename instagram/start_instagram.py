import scrapy.cmdline

filepath = './data.json'
scrapy.cmdline.execute(f'scrapy crawl instagram_spider -o {filepath}'.split(' '))
