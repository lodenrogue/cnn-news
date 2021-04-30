import unittest
from cnn_news import CnnNews
import json


class CnnNewsTest(unittest.TestCase):

    def test_returns_correct_article_count(self):
        count = 3
        articles = CnnNews().get_articles(count)
        self.assertTrue(len(articles) is count, "Articles has correct article count")


    def test_returns_values_for_articles(self):
        articles = CnnNews().get_articles(3)
        self.assertTrue(len(articles) > 0, "Article list is not empty")

        for article in articles:
            print(json.dumps(article.__dict__))
            self.assertIsNotNone(article.url, "Article url is not None")
            self.assertIsNotNone(article.title, "Article title is not None")
            self.assertIsNotNone(article.snippet, "Article snipper is not None")


if __name__ == '__main__':
    unittest.main()
