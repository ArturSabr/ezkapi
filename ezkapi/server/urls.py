from django.urls import path
from .views import *


urlpatterns = [
    path('user/update/<int:pk>', UserUpdateView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('auth/', NewAuthView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyCustomView.as_view()),
    path('user/change_password/', ChangePasswordView.as_view()),
    path('schedule/', DesciplineSheduleView.as_view())
]
