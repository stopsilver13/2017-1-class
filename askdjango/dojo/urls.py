from django.conf.urls import url
from dojo import views

urlpatterns = [
    url(r'^sum/(?P<x>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^json_response/$', views.json_response),
    url(r'^yagudjango_team.jpg/$', views.image_download),
    url(r'^yagudjango_team.jpg/title/$', views.image_download_write_title),
]