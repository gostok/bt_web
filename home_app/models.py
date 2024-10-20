from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.alt_text

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SidebarNews(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title