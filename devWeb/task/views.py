from django.shortcuts import render

# Create your views here.

#Home
def home(request):
  return render(request, 'home.html')

#SignUp
def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html')
  else:
    if request.POST['password1'] == request.POST['password2']
    try:
      user = User.objects.create_user(username)

#SignIn
def signin(request):
  return render(request, 'signin.html')