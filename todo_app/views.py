from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from todo_app.models import Task


class TaskList(LoginRequiredMixin, ListView):
    """TaskList
    https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview
    """
    model = Task
    context_object_name = 'tasks'  # templateでの変数名を変える


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # 作成対象フィールド
    fields = '__all__'  # ['user', 'title', ...]と同じ
    # 作成後のリダイレクト
    success_url = reverse_lazy('tasks')  # urls.pyでのページ名と対応


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # 更新対象フィールド
    fields = '__all__'  # ['user', 'title', ...]と同じ
    success_url = reverse_lazy('tasks')  # urls.pyでのページ名と対応


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskListLoginView(LoginView):
    fields = '__all__'
    # デフォルトはregistration/login.htmlなのでカスタマイズする
    template_name = 'todo_app/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks')
