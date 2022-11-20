from django.test import RequestFactory,TestCase
from .models import Page
from django.contrib.auth.models import AnonymousUser, User


# Create your tests here.
class PageTestCase(TestCase):
    def setUp(self):
        # Create a Test User
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@kamyar_mk.com', password='top_secret'
        )
        # Making the Categories
        Page.objects.create(Title="Test Page 1", Slug="test_page_1", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)
        Page.objects.create(Title="Test Page 2", Slug="test_page_2", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)
        Page.objects.create(Title="Test Page 3", Slug="test_page_3", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)
        Page.objects.create(Title="Test Page 4", Slug="test_page_4", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)
        Page.objects.create(Title="Test Page 5", Slug="test_page_5", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)
        Page.objects.create(Title="Test Page 6", Slug="test_page_6", Status="P", Content=" this is a test content", Parent=0, OwnerId=self.user)

    def test_page_retrive(self):
        """Test if the Pages are saved Correctly"""
        self.assertEqual(Page.objects.get(id=1).Slug, 'test_page_1')
        self.assertEqual(Page.objects.get(id=2).Slug, 'test_page_2')
        self.assertEqual(Page.objects.get(id=3).Slug, 'test_page_3')
        self.assertEqual(Page.objects.get(id=4).Slug, 'test_page_4')
        self.assertEqual(Page.objects.get(id=5).Slug, 'test_page_5')
        self.assertEqual(Page.objects.get(id=6).Slug, 'test_page_6')