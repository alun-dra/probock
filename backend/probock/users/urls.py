from rest_framework import routers
from django.urls import include, path

from users.views.userView import UsersViewset

user_router = routers.SimpleRouter(trailing_slash=False)

user_router.register(r'userEnpoit', UsersViewset, basename='re_users')

app_name = 'users'

urlpatterns = [
    path('users/', include(user_router.urls)),
    path('users/<int:pk>/', UsersViewset.as_view({'get': 'GetUserById'}), name='user-detail'),
]
