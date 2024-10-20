from django.db import models

from home_app.models import SidebarNews

class TattooSidebarNews(SidebarNews):
    pass

class Tattoo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.ImageField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Master(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.ImageField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
