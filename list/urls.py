from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.nominee_list, name='nominee_list')
]
