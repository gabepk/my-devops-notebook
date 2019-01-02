from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_roadmap, name="roadmap"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
]