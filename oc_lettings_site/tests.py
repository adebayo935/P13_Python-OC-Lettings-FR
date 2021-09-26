from django.test import TestCase
from django.urls import reverse


def test_dummy():
    assert 1


class TestIndex(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_index = '/index_test'
        cls.url_index = reverse("index")

    def test_index(self):
        print('\n testing a bad url')
        result = self.client.get(self.test_index)
        assert result.status_code in [404]

    def test_url_index(self):
        print('\n testing index url')
        result = self.client.get(self.url_index)
        assert result.status_code in [200]
