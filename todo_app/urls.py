from django.urls import path

from .views import TaskCreate, TaskList, TaskDetail


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),  # PrimaryKeyの動的URL
    path('create-task', TaskCreate.as_view(), name='create-task'),  # PrimaryKeyの動的URL
]
