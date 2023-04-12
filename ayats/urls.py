from django.urls import include, re_path
from ayats import views 
 
 
urlpatterns = [ 
    re_path(r'^api/ayats$', views.detail_ayat),
    re_path(r'^api/ayats/(?P<pk>[0-9]+)$', views.detail_list_ayat)
    # url(r'^api/surats/published$', views.tutorial_list_published)
]
