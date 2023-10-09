from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from todo_app.models import Task


class TaskList(ListView):
    """TaskList
    https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview
    """
    model = Task
