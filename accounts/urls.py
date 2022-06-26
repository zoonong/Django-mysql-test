from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('mypage/<int:id>', mypage, name="mypage"),
    path('<int:id>/follow', follow,name="follow"),
]