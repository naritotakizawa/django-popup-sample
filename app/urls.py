from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post_create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^category_create/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^tag_create/$', views.TagCreate.as_view(), name='tag_create'),

    url(r'^popup/category_create/$',
        views.PopupCategoryCreate.as_view(),
        name='popup_category_create'
    ),
    url(r'^popup/tag_create/$',
        views.PopupTagCreate.as_view(),
        name='popup_tag_create'
    ),
]
