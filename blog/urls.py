from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('latest/feed/', LatestPostsFeed(), name='feed'),
    # tag url
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share')
]