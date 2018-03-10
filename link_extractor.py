import re


class extractor:
    def __init__(self, html,feed):
        self.html = html
        self.feed = feed
      
    def ext(self):
        pattern = re.compile(self.html)
        for line in pattern.findall(self.feed.content):
            print line+'\n'
