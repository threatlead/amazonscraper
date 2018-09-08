from .context import amazonscraper
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_scraper(self):
        data = amazonscraper.AmazonScraper.scrape('B003F2X13I')
        self.assertEqual(data['asin'], 'B003F2X13I', 'Invalid Response from Amazon.')


if __name__ == '__main__':
    unittest.main()
