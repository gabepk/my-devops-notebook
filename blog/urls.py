from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.render_roadmap, name="roadmap"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]