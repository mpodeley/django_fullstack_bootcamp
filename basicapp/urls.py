from django.conf.urls import url
from basicapp import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.first_app,name='first_app'),
    path('', views.index, name='index'),
    path('form/', views.form_name_view, name='form_name'),
]
