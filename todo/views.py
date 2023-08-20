from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import ToDoList
# Create your views here.



def home(request):
    if request.GET.get('user'):
        user=request.GET.get('user')
        login(request,user)
    return render(request,'index.html')


def SignUp(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        if  User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Taken')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already In Use')
            return redirect('signup')   
        
        user=User.objects.create(
            username=username,
            email=email)
        user.set_password(password)
        login(request,user)
        return redirect('home')



def user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        username=request.POST.get('username')
        pasword=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Not a valid username')
            return redirect('login')   
        user=authenticate(username=username,password=pasword)

        if user is not None:
            login(request,user)
            return redirect('home')
        messages.info(request,'Wrong Password')
        return redirect('login')



def mytodos(request,user_todo):
    user=User.objects.get(username=user_todo)
    user_todos=ToDoList.objects.filter(user=user.id)
    context={
        'todos':user_todos
    }
    return render(request,'todos.html',context)



def add_todo(request):
    if request.method=='POST':  
      todo=request.POST.get('todo')
      username=request.POST.get('user')
      user=User.objects.get(username=username)
      new_todo=ToDoList(title=todo,user=user)
      new_todo.save()
      messages.success(request,'Todo Added Sucessfully')

    return redirect(f'mytodos/{username}')
    


def remove_todo(request):
    if request.method=='POST':   
       username=request.POST.get("user")
       print(username)
       todo_id=request.POST.get('todoid')
       print(todo_id)
       user=User.objects.get(username=username)
       todos=ToDoList.objects.get(sn=todo_id,user=user)
       todos.delete()
       messages.success(request,'Todo Deleted Sucessfully')
    return redirect(f'mytodos/{username}')


    
