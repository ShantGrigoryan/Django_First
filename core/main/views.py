from django.shortcuts import render, redirect
from .models import TodoList

# Create your views here.
# TODO_PATH = 'main/TODO_SAVES/todo_list.txt'

# def index(request):
#     if request.method == "POST":
#         info = request.POST.get('info')
#         todo_delete = request.POST.get('todo_id')
#         if info == None:
#             with open(TODO_PATH, 'r') as file:
#                 res = file.read()
#             res = res.split('\n')
#             res.remove(todo_delete)
#             print(res)
#             with open(TODO_PATH, 'w') as file:
#                 file.write('')
#             with open(TODO_PATH, 'a') as file:
#                 for i in res:
#                     file.write(f'{i}\n')
#         else:
#             with open(TODO_PATH, 'a') as file:
#                 file.write(f'{info}\n')
#         return redirect('index')
#     else:
#         with open(TODO_PATH, 'r') as file:
#             res = file.read()
#         res = res.split('\n')
#         return render(request, 'main/index.html', context={
#             'todo_list':res  
#         })


def index(request):
    if request.method == 'POST':
        info = request.POST.get('info')
        delete_id = request.POST.get('todo_id')
        if info == None:
            TodoList.objects.filter(id=delete_id).delete()
        else:
            TodoList.objects.create(name=info)
        return redirect('index')
    todoList = TodoList.objects.all()
    return render(request, 'main/index.html', context={
        'todolist':todoList
    })