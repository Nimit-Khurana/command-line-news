# Extraction from tribune
# url 'http://www.tribuneindia.com/news/nation/'


import requests
from link_extractor import extractor

class newspaper:
    def hindu(self):
        link = r'<a href="http://www.thehindu.com/news/national/(.+?).ece"'
        feed = requests.get('http://www.thehindu.com/news/national')
        x = extractor(link,feed)
        print x.ext()

    def tribune(self):
        link = r'<a href="http://www.tribuneindia.com/news/nation/(.+?).html"'
        feed = requests.get('http://www.tribuneindia.com/news/nation/')
        x = extractor(link,feed)
        print x.ext()
            
    def express(self):
        link = r'<a href="http://indianexpress.com/article/india/(.+?)>"'
        feed = requests.get('http://indianexpress.com/section/india/')
        x = extractor(link,feed)
        print x.ext() 
