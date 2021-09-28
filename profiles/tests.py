from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class TestProfiles(TestCase):
    @classmethod
    def setUp(cls):
        test_user = User.objects.create(username="usertest")
        cls.test_profile = Profile.objects.create(
            favorite_city="testcity",
            user=test_user
        )

    @classmethod
    def tearDownClass(cls):
        Profile.objects.all().delete()

    def test_url(self):
        print('\n testing profile index')
        url_profiles = reverse('profiles_index')
        result = self.client.get(url_profiles)
        # assert result.status_code in [200]
        self.assertContains(result, '<title>Profiles</title>', status_code=200)

    def test_profile(self):
        print('\n testing profile view')
        url_profile = reverse('profile', args=[self.test_profile])
        result = self.client.get(url_profile)
        # assert result.status_code in [200]
        self.assertContains(result, f'<title>{self.test_profile}</title>', status_code=200)
