from django.urls import path
from .views import get_user, create_user, user_detail

urlpatterns= [
    path('user/',get_user ,name='get_users'),
    path('user/create/',create_user ,name='create _user'),
    path('user/<int:pk>',user_detail ,name='user_detail'),

]
