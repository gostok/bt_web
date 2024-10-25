from django.db import models
from home_app.models import SidebarNews, HeaderImage


class SessionHeaderImage(HeaderImage):
    pass


class SessionSidebarNews(SidebarNews):
    pass


class AvailableDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class AvailableTime(models.Model):
    date = models.ForeignKey(
        AvailableDate, on_delete=models.CASCADE, related_name="available_times"
    )
    time = models.TimeField()

    def __str__(self):
        return str(self.time)


class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
