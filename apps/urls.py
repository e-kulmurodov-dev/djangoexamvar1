# ------------- email verification ---------
from django.urls import path

from apps.views import signup, account_activation_sent, activate, account_activation_complete, LoginView, UserListView, \
     UserProfile

urlpatterns = [
    path('', signup, name='signup'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('account_activation_complete/', account_activation_complete, name='account_activation_complete'),
    path('accounts/login/', LoginView.as_view(
        next_page='user_detail'
    ), name='login'),
    path('', UserListView.as_view(), name='blog_list_page'),
    path('user-detail/<int:pk>', UserProfile.as_view(), name='user_detail'),
]
