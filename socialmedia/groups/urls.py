# groups urls.py 

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^/$", views.ListGroups.as_view(), name="all"),
    url(r"^new/$", views.CreateGroup.as_view(), name="create"),
    url(r"^posts/in/(?P<slug>[-\w]+)/$", views.SingleGroup.as_view(), name="single"),
    
]
