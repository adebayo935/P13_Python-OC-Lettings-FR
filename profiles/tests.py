from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class TestProfiles(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_user = User.objects.create(username="usertest")
        cls.test_profile = Profile.objects.create(
            favorite_city="testcity",
            user=cls.test_user
        )
        cls.url_profiles = reverse('profiles:profiles_index')
        cls.url_profile = reverse('profiles:profile', args=[cls.test_profile])
        cls.no_profile = reverse('profiles:profile', args=["usernone"])

    @classmethod
    def tearDownClass(cls):
        Profile.objects.all().delete()

    def test_url(self):
        print('\n testing profile index')
        result = self.client.get(self.url_profiles)
        assert result.status_code in [200]

    def test_profile(self):
        print('\n testing profile view')
        result = self.client.get(self.url_profile)
        assert result.status_code in [200]

    def test_no_profile(self):
        print('\n testing unknown profile view')
        result = self.client.get(self.no_profile)
        assert result.status_code in [404]
