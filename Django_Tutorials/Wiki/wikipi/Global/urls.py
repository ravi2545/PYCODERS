from django.urls import path
from .views import *

urlpatterns = [
    path("all/", all.as_view()),
]