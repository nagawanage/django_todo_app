from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from todo_app.models import Task


class TaskList(ListView):
    """TaskList
    https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview
    """
    model = Task
    context_object_name = 'tasks'  # templateでの変数名を変える


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    # 作成対象フィールド
    fields = '__all__'  # ['user', 'title', ...]と同じ
    # 作成後のリダイレクト
    success_url = reverse_lazy('tasks')  # urls.pyでのページ名と対応


class TaskUpdate(UpdateView):
    model = Task
    # 更新対象フィールド
    fields = '__all__'  # ['user', 'title', ...]と同じ
    success_url = reverse_lazy('tasks')  # urls.pyでのページ名と対応


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
