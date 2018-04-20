from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.PostListView.as_view(), name='post_list'),
    url(r'^post/new1/$', views.post_new1, name='post_new'),
    url(r'^post/new2/$', views.PostNewView.as_view(), name='postNew'),
    url(r'^post/list/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/update/(?P<pk>[0-9]+)/$', views.PostUpdateView.as_view(), name='updateblog'),
]