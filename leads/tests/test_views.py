from django.test import TestCase
from django.urls import reverse_lazy


class LandingPageTest(TestCase):
    
    def test_get(self):
        response = self.client.get(reverse_lazy('landing-page'))
        # print(response.content)
        self.assertEqual(response.status_code,200)
        self.assertTemplateNotUsed(response, 'landing-page')
