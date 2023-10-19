from django.shortcuts import render

# Create your views here.

#Home
def home(request):
  return render(request, 'home.html')

#SignUp
def signup(request):
  return render(request, 'signup.html')

#SignIn
def signin(request):
  return render(request, 'signin.html')