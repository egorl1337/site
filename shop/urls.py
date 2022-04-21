from django import views
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index_shop, name = 'index_shop'),
    path('/comments/', views.comments, name = 'comments'),
    path('<int:pk>', views.New_detail_view.as_view(), name = 'detail_view'),
    path('/comments/<int:pk>/edit', views.edit_comment.as_view(), name = 'comment_edit')   
]


