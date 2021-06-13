from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('content/', views.content, name='content'),
    path('ideas/', views.ideas, name='ideas'),
    path('join_us/', views.join_us, name='join_us'),
    path('studio/', views.studio, name='studio'),




]