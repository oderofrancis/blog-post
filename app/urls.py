from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('post/',post,name='post'),
    path('post_view/',post_view,name='post_view'),
]