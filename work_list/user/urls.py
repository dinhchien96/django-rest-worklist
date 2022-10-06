from django.urls import path, include
from user import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('delete/', views.DeleteUserview.as_view(), name='user-delete'),
    path('view/', views.Userview.as_view(), name='user-detail'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]