from django.urls import path
from .views import UserCreationView , UserLoginView , UserLogoutView , UserBankAccountUpdateView
urlpatterns = [
    path('register/', UserCreationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
]