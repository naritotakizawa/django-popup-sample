from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post_create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^category_create/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^tag_create/$', views.TagCreate.as_view(), name='tag_create'),
]
