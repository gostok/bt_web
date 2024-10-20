from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("session/", BookSessionView.as_view(), name="session"),
    path("get-times/", get_times, name="get_times"),
]
