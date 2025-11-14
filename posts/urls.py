from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    MeView,
    PasswordChangeView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Auth
    path('auth/login/', LoginView.as_view(), name='api_login'),
    path('auth/logout/', LogoutView.as_view(), name='api_logout'),
    path('auth/me/', MeView.as_view(), name='api_me'),
    path('auth/password-change/', PasswordChangeView.as_view(), name='api_password_change'),

    # Posts CRUD
    path('posts/', PostListCreateView.as_view(), name='api_post_list_create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='api_post_detail'),
]
