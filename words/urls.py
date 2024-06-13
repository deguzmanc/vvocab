from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("submitlink/", views.submitlink, name="submitlink"),
    path("gettranscript/", views.gettranscript, name="gettranscript"),
]