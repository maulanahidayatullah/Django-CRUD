from django.urls import path
from .views import get_users, create_users, user_detail

urlpatterns = [
    path('users/', get_users),
    path('users/create', create_users),
    path('users/<int:pk>', user_detail),
]