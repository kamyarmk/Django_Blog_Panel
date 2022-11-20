from django.conf import settings
from django.db import models
import django.utils.timezone as DjangoTime


# Create your models here.

class Page(models.Model):
    status = (
        ('P', 'Published'),
        ('H', 'Hidden'),
        ('D', 'Deleted')
    )
    Title = models.CharField(max_length=50)
    Slug = models.CharField(max_length=100)
    Date = models.DateField(default=DjangoTime.now())
    Status = models.CharField(max_length=1, choices=status)
    Content = models.TextField()
    Parent = models.IntegerField(default=0)
    OwnerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title