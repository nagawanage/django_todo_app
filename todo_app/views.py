from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todo_app.models import Task


class TaskList(LoginRequiredMixin, ListView):
    """TaskList
    https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview
    """
    model = Task
    context_object_name = 'tasks'  # templateでの変数名を変える

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
        """
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # print(f'TaskList: {context=}')

        # 検索機能対応
        search_input_text = self.request.GET.get('search') or ''  # 検索結果がNoneなら空白
        if search_input_text:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input_text)
            # print(f'{search_input_text=}')

        context['search'] = search_input_text

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # 作成対象フィールド
    fields = ['title', 'description', 'completed']
    # 作成後のリダイレクト
    success_url = reverse_lazy('tasks')  # urls.pyでのページ名と対応

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """ログインユーザーのデータのみ作成可能にする"""
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class RegisterUser(FormView):
    """アカウント新規登録"""
    template_name = 'todo_app/register.html'
    form_class = UserCreationForm  # ユーザー登録formに設定
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: Any) -> HttpResponse:
        # アカウント登録
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)
