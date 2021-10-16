from django.urls import path
from account.views import *

app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate'),
    # path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]