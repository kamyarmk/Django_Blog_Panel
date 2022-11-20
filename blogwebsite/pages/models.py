from django.conf import settings
from django.db import models

# Create your models here.

class Page(models.Model):
    status = (
        ('P', 'Published'),
        ('H', 'Hidden'),
        ('D', 'Deleted')
    )
    Title = models.CharField(max_length=50)
    Date = models.DateField()
    Status = models.CharField(max_length=1, choices=status)
    Content = models.CharField(max_length=250)
    OwnerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.PostTitle