from django.conf.urls import url
from second_app import views
from django.urls import path
app_name = 'second_app'
urlpatterns = [
    #url(r'^$', views.first_app,name='first_app'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),

    #path('login/', views.login, name='login'),
]
