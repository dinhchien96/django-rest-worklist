from django.urls import path, include
from work import views
# from .views 



urlpatterns = [
    path('create/', views.CreateTask.as_view(), name='create-task'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update-task'),
    path('task-delete/<int:pk>/', views.DeleteTask.as_view(), name='delete-task'),
    path('task/<int:pk>/', views.ViewTask.as_view(), name='view-task-detail'),
    path('task/', views.ViewTask.as_view(), name='view-task'),
]