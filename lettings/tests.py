from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class TestLettings(TestCase):
    @classmethod
    def setUp(cls):
        test_address = Address.objects.create(
            number=42,
            street='none',
            city='none',
            state='none',
            zip_code=00000,
            country_iso_code='XX'
        )
        cls.test_letting = Letting.objects.create(
            title="test",
            address=test_address
        )

    @classmethod
    def tearDownClass(cls):
        Address.objects.all().delete()
        Letting.objects.all().delete()

    def test_url(self):
        print('\n testing letting index')
        url_lettings = reverse('lettings_index')
        result = self.client.get(url_lettings)
        assert result.status_code in [200]

    def test_letting(self):
        print('\n testing letting view')
        url_letting = reverse('letting', args=[self.test_letting.id])
        result = self.client.get(url_letting)
        assert result.status_code in [200]
