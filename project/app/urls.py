from django.urls import path
from .views import UserProfileListCreateView, ShiftListCreateView, OrderListCreateView, ProductListCreateView, UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('userprofiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('shift/', ShiftListCreateView.as_view(), name='shift-list-create'),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
]