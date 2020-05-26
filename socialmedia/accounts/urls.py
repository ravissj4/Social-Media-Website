from django.conf.urls import urls
from django.contrib.auth import views as auth_views
from . import views

url_patterns = [
    url(r"^login/$", 
        auth_views.LoginView.as_view(template="accounts/login.html"), 
        name="login"),
    url(r"^logout/$", LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    
]