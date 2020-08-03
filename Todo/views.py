from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from .models import Todo


def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'index.html', {'all_todos': all_todos})


def create(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        target_date = request.POST['target_date']
        todo, created = Todo.objects.get_or_create(
            todo=todo, date_target=target_date)
        print(todo, created)

    return redirect('/todo')
