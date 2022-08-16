from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_mainpage, name='hello_mainpage'),
    path('about', views.about, name='about'),
    path('cool_page', views.cool_page, name='cool_page'),
    path('addition', views.addition, name = 'addition'),
    path('add_post', views.add_post, name = 'add_post'),
]