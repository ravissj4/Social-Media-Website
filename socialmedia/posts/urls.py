from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
    url(r"new/$", views.CreatePost.as_view(), name="create"),
    # url will be something like posts/by/user's slug pattern
    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    # url -> posts/by/user's slug/post id
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    # url -> posts/delete/post id
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]
