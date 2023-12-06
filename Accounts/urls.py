from django.urls import path
from .views import *

urlpatterns = [
    path("add_education",add_education,name="add_education"),
    path("add_experience",add_experience,name="add_experience"),
    path("create_profile",create_profile,name="create_profile"),
    path("dashboard",dashboard,name="dashboard"),
    path("login",login,name="login"),
    path("profile",profile,name="profile"),
    path("profiles",profiles,name="profiles"),
    path("register",register,name="register"),
]
    