from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class TestLettings(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_address = Address.objects.create(
            number=42,
            street='none',
            city='none',
            state='none',
            zip_code=00000,
            country_iso_code='XX'
        )
        cls.test_letting = Letting.objects.create(
            title="test",
            address=cls.test_address
        )
        cls.url_lettings = reverse('lettings:lettings_index')
        cls.url_letting = reverse('lettings:letting', args=[cls.test_letting.id])
        cls.no_letting = reverse('lettings:letting', args=[0])
        # print(f' {}')
        # print(f'cls.test_address {cls.test_address}')
        # print(f'cls.test_letting {cls.test_letting}')
        # print(f'cls.url_lettings {cls.url_lettings}')
        # print(f'cls.url_letting {cls.url_letting}')
        # print(f'cls.no_letting {cls.no_letting}')

    @classmethod
    def tearDownClass(cls):
        Address.objects.all().delete()
        Letting.objects.all().delete()

    def test_url(self):
        print('\n testing letting index')
        result = self.client.get(self.url_lettings)
        assert result.status_code in [200]

    def test_letting(self):
        print('\n testing letting view')
        result = self.client.get(self.url_letting)
        assert result.status_code in [200]

    def test_no_letting(self):
        print('\n testing unknown letting view')
        result = self.client.get(self.no_letting)
        assert result.status_code in [404]
