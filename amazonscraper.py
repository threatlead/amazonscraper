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
        # -- price
        list_price = doc("div#price > table").find('tr').eq(0).find('td').eq(1).find('span').eq(0).text().strip('$')
        list_price = float(list_price) if list_price is not '' else None
        price = doc("div#cerberus-data-metrics").attr('data-asin-price')
        price = float(price) if price is not '' else None
        asin = doc("div#cerberus-data-metrics").attr('data-asin')
        brand = doc("div#mbc").attr('data-brand')
        features = [li.text().strip('[\\n\\t]') for li in doc("div#feature-bullets").find('li').items()]
        editorial_review = doc("div#productDescription").find('p').eq(0).text().strip('[\\n\\t ]')
        # -- images
        img_url = doc("img#landingImage").attr('data-old-hires')
        if '.jpg' not in img_url:
            img_url = doc("img#landingImage").attr('data-a-dynamic-image')
            match = re.findall('https://.*?amazon.com/images/I/.*?\._[A-Z0-9]{5,}_\.jpg', img_url)
            img_url = match[0] if '.jpg' in match[0] else None
        if img_url:
            large_img_url = re.sub(r'\._S[A-Z0-9]+_\.jpg$', '.jpg', img_url)
            medium_img_url = re.sub(r'\.jpg$', '._SL160_.jpg', large_img_url)
            small_img_url = re.sub(r'\.jpg$', '._SL75_.jpg', large_img_url)
        else:
            large_img_url, medium_img_url, small_img_url = None, None, None
        # -- star rating
        rating = doc('span#acrPopover').attr('title')
        if 'out of 5 stars' in rating:
            rating = float(rating.strip('out of 5 stars'))
        else:
            rating = None
        # --
        review_count = doc('span#acrCustomerReviewText').html()
        if 'customer reviews' in review_count:
            review_count = int(review_count.strip('customer reviews'))
        else:
            review_count = None
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
            'rating': rating,
            'review_count': review_count,
        }

    @classmethod
    def scrape(cls, asin):
        url = "http://www.amazon.com/dp/" + asin
        page = requests.get(url, headers={'User-Agent': cls.ua.opera})
        if page.status_code != 200:
            return None
        data = cls.html_parse(page.content)
        return data


if __name__ == '__main__':
    data = AmazonScraper.scrape('B01J42JPJG')
    print(data)
