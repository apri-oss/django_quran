from django.urls import include, re_path
from surats import views 
 
 
urlpatterns = [ 
    re_path(r'^api/surats$', views.surat_list)
    # url(r'^api/surats/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/surats/published$', views.tutorial_list_published)
]
