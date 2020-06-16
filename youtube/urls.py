from django.urls import path 
from . import views
app_name = 'youtube'

urlpatterns = [
    path('',views.index,name='index'),
    path('upload/',views.uploads,name='upload'),
]
