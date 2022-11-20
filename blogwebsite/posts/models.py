from django.conf import settings
from django.db import models
from datetime import date
import django.utils.timezone as DjangoTime

# Blogs are part of the main system which they have **Title, Content , featured Images, publish date, Status, Category, Tags, Author**  and later they are going to have meta field such as **************************Keyword, Desc.**************************
# We have the option to make a custom **********Slug********** or it’s going to generate from the title of the page.
# Media is going to Copy the name of the File in the Database
# Last Edited on 26/10/2022 on 4:36
# Created at 26/10/2022 on 4:36
# Edits : 1


class Category(models.Model):
    # Main Attributes
    Name = models.CharField(max_length=50)
    Slug = models.CharField(max_length=100, unique=True)
    Parent = models.IntegerField(default=0)
    # General Tags
    Date = models.DateField(default=DjangoTime.now())
    # SEO Tags
    Meta_Keyword = models.CharField(max_length=50)
    Meta_Desc = models.CharField(max_length=250)

    def ordering_categorys_parent():
        all_category = Category.objects.all()
        ordered_category = {}
        for category in all_category:
            if(category.Parent != 0):
                if( category.Parent in ordered_category):
                    ordered_category[category.Parent].append(category.id)
                else:
                    ordered_category[category.Parent] = [category.id]
            else:
                ordered_category[category.id] = []
        return ordered_category;

    def __str__(self):
        return self.Name



class Tag(models.Model):
    #  Main Attributes
    Name = models.CharField(max_length=50)
    Slug = models.CharField(max_length=100, unique=True)
    #General Tags
    Date = models.DateField(default=DjangoTime.now())
    # SEO Tags
    Meta_Keyword = models.CharField(max_length=50)
    Meta_Desc = models.CharField(max_length=250)

    def __str__(self):
        return self.Name


class Post(models.Model):
    status = (
        ('P', 'Published'),
        ('H', 'Hidden'),
        ('D', 'Deleted')
    )
    # Main Attributes
    Title = models.CharField(max_length=50)
    Slug = models.CharField(max_length=100, unique=True)
    Category = models.ManyToManyField(Category)
    Tags = models.ManyToManyField(Tag)
    Status = models.CharField(max_length=1, choices=status)
    Text = models.TextField()
    Featured_Image = models.FileField()
    # General Tags
    Date = models.DateField(default=DjangoTime.now())
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # SEO Tags
    Meta_Keyword = models.CharField(max_length=50)
    Meta_Desc = models.CharField(max_length=250)

    def __str__(self):
        return self.Title


