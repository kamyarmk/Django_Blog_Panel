from django.test import TestCase
from .models import Post, Category, Tag

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        # Making the Categories
        Category.objects.create(Name="test1",Slug="test1",Parent="0")
        Category.objects.create(Name="test2",Slug="test2",Parent='1')
        Category.objects.create(Name="test3",Slug="test3",Parent="0")
        Category.objects.create(Name="test4",Slug="test4",Parent="0")
        Category.objects.create(Name="test5",Slug="test5",Parent='3')
        Category.objects.create(Name="test6",Slug="test6",Parent='1')
        # Making the Tags
        Tag.objects.create(Name="Tag1", Slug="tag1")
        Tag.objects.create(Name="Tag2", Slug="tag2")
        Tag.objects.create(Name="Tag3", Slug="tag3")
        Tag.objects.create(Name="Tag4", Slug="tag4")
        Tag.objects.create(Name="Tag5", Slug="tag5")
        # Making Posts
        Post.objects.create(Title="Test Post 1",Slug="test_post_1",Category=1,Tags=[1,2],Status="P",Text="something something",Author=1)
        Post.objects.create(Title="Test Post 2",Slug="test_post_2",Category=3,Tags=[4,2],Status="P",Text="something something",Author=1)
        Post.objects.create(Title="Test Post 3",Slug="test_post_3",Category=4,Tags=[3,2],Status="P",Text="something something",Author=1)
        Post.objects.create(Title="Test Post 4",Slug="test_post_4",Category=5,Tags=[1,5],Status="P",Text="something something",Author=1)
        Post.objects.create(Title="Test Post 5",Slug="test_post_5",Category=2,Tags=[3,4],Status="P",Text="something something",Author=1)
        Post.objects.create(Title="Test Post 6",Slug="test_post_6",Category=1,Tags=[5,2],Status="P",Text="something something",Author=1)

    def test_category_order(self):
        """Test if the Categories are ordered Correctly"""
        self.assertEqual(Category.ordering_categorys_parent(), {1: [2, 6],3: [5],4: []})
        
    def test_categry_retrive(self):
        """Test if the Categories are ordered Correctly and the names are correctly"""
        ordered_category = list(Category.ordering_categorys_parent().keys())
        test_category = Category.objects.get(id=ordered_category[0])
        self.assertEqual(test_category.Name, 'test1')

    def test_tag_retrive(self):
        """Test if the Tags are saved Correctly"""
        self.assertEqual(Tag.objects.get(id=1).Name, 'Tag1')
        self.assertEqual(Tag.objects.get(id=1).Slug, 'tag1')

    def test_post_retrive(self):
        """Test if the Tags are saved Correctly"""
        self.assertEqual(Tag.objects.get(id=1).Slug, 'tag1')