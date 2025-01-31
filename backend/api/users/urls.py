from django.urls import path

from .views import UserList, UserDetail


urlpatterns = [
    # main page index
    path('', UserList.as_view(), name='user_list'),
    path('<str:username>/', UserDetail.as_view(), name='user_detail')
]