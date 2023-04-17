from django.urls import include, re_path
from homepages import views 
 
 
urlpatterns = [ 
    re_path('', views.home)
]
