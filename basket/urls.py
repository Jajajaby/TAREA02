from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
    path('add/', views.add, name="player_add"),
    path('list2', views.list2, name="player_list2"),
]
