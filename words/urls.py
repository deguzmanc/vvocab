from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/signup/', views.user_signup, name='signup'),
    # path('accounts/')
    path('logout/', views.user_logout, name='logout'),
    path("submitlink/", views.submitlink, name="submitlink"),
    path("gettranscript/", views.gettranscript, name="gettranscript"),
    path('video/', views.video, name='video-page'),
    path('video/<int:id>/', views.video, name='video'),
    path('accounts/profile/', views.profile, name='profile'),
]
