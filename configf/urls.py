from django.urls import path
from configf.views import *

urlpatterns = [
    path('index/', index, name="Home"),
    path('category/<int:pk>/',category, name="category"),
]