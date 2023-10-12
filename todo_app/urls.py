from django.urls import path

from .views import TaskCreate, TaskList, TaskDetail, TaskUpdate, TaskDelete, TaskListLoginView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),  # PrimaryKeyの動的URL
    path('create-task', TaskCreate.as_view(), name='create-task'),  # PrimaryKeyの動的URL
    path('edit-task/<int:pk>', TaskUpdate.as_view(), name='edit-task'),  # PrimaryKeyの動的URL
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),  # PrimaryKeyの動的URL
    path('login', TaskListLoginView.as_view(), name='login'),
]
