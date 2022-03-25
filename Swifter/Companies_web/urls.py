from django.contrib import admin
from django.urls import path
from Companies_web import views
urlpatterns = [
  path('signup',views.Signup, name="signup"),
  path('login',views.login, name="login"),
  path('logout',views.logout, name="logout"),
]
