from pyquery import PyQuery as pq
import re
from fake_useragent import UserAgent
import requests


class AmazonScraper:
    ua = UserAgent()

    @classmethod
    def html_parse(cls, html):
        doc = pq(html)
        title = doc("h1#title").text().strip('[\\n ]')
        list_price = doc("div#price > table").find('tr').eq(0).find('td').eq(1).find('span').eq(0).text().strip('$')
        list_price = float(list_price)
        price = float(doc("div#cerberus-data-metrics").attr('data-asin-price'))
        asin = doc("div#cerberus-data-metrics").attr('data-asin')
        brand = doc("div#mbc").attr('data-brand')
        features = [li.text().strip('[\\n\\t]') for li in doc("div#feature-bullets").find('li').items()]
        editorial_review = doc("div#productDescription").find('p').eq(0).text().strip('[\\n\\t ]')
        # -- images
        large_img_url = doc("img#landingImage").attr('data-old-hires')
        large_img_url = re.sub(r'\._SL[0-9]+_\.jpg$', '.jpg', large_img_url)
        medium_img_url = re.sub(r'\.jpg$', '._SL160_.jpg', large_img_url)
        small_img_url = re.sub(r'\.jpg$', '._SL75_.jpg', large_img_url)
        # --
        return {
            'asin': asin,
            'title': title,
            'editorial_review': editorial_review,
            'features': features,
            'brand': brand,
            'large_img_url': large_img_url,
            'medium_img_url': medium_img_url,
            'small_img_url': small_img_url,
            'list_price': list_price,
            'price': price,
        }

    @classmethod
    def scrape(cls, asin):
        url = "http://www.amazon.com/dp/" + asin
        page = requests.get(url, headers={'User-Agent': cls.ua.opera})
        if page.status_code != 200:
            return None
        data = cls.html_parse(page.content)
        return data
