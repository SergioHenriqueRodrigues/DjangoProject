from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

#Home
def home(request):
  return render(request, 'home.html')

#SignUp
def signup(request):
  if request.method == 'GET':
    return render(request,'signup.html', {
      'form' : UserCreationForm
    } )   
  else: 
    if request.POST['password1'] == request.POST['password2']:
      try: 
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()                
        login(request, user)
        return redirect('tasks')
      except:
        return render (request,'signup.html', { 
          'form' : UserCreationForm ,
          "error": 'Usuário já existe'                
        } ) 
    return render (request,'signup.html', { 
      'form' : UserCreationForm ,
      "error": 'senhas são diferentes'
    } ) 

#SignIn
def signin(request):
  if request.method == 'GET':
    return render(request,'signin.html', {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(
      request, username=request.POST['username'], password=request.POST['password']
    )
    if user is None:
      return render(request, 'signin.html', {
        'form' : AuthenticationForm,
        'error': 'Usuário ou senha está incorreto'
      })
    else:
      login(request, user)
      return redirect('tasks')

#Sair
@login_required
def sair(request):
  logout (request)
  return redirect('home')

#Tasks
@login_required
def tasks(request):
  return render(request, 'tasks.html')

@login_required  
def criandoTarefa(request):
    
    if request.method == 'GET':
        return render(request, 'criandoTarefa.html', {
            'form' : TaskForm
        })

    else:

        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')

        except ValueError:

            return render(request,'criandoTarefa.html', {
                'form' : TaskForm,
                'error' : 'Favor inserir dados validos'
            })      