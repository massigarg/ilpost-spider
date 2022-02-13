# from urllib import response
import scrapy
import re


class IlPostScraper(scrapy.Spider):
    name = "ilpost"
    start_urls = ["https://www.ilpost.it/italia/"]
    # custom_settings = {
    #     "FEEDS": {"ilpost.json": {"format": "json", "encoding": "utf8"}},
    # }  # or use scrapy crwal -O (caps o override) ilpost.json

    def parse(self, resposne):

        # category pattern
        category_pattern = r"category-([a-z0-9-]+)"
        regex_category = re.compile(category_pattern)

        # tag pattern
        tag_pattern = r"tag-([a-z0-9-]+)"
        regex_tag = re.compile(tag_pattern)
        #re.findall( r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')

        # date patern
        date_pattern = r".{22}(.{10}).*"
        regex_date = re.compile(date_pattern)
        for article in resposne.css("article.home"):
            try:
                headline = article.css("h2 a::text").get()
            except:
                headline = None

            try:
                summary = article.css("p a::text").get()[:-1]
            except:
                summary = None

            try:
                category = regex_category.findall(
                    article.css("::attr(class)").get())
            except:
                category = None

            try:
                tag = regex_tag.findall(article.css("::attr(class)").get())
            except:
                tag = None
            try:
                date = (regex_date.findall(article.css(
                    "p a").attrib["href"])[0]).replace("/", "-")
            except:
                date = None

            yield {date[:4]: {
                "headline": headline,
                "summary": summary,
                "category": category,
                "tag": tag,
                "date": date
            }
            }

            next_page = resposne.css("a.next.page-numbers").attrib["href"]
            if next_page is not None:
                yield resposne.follow(next_page, callback=self.parse)
