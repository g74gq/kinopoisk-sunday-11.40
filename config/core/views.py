from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login, logout 
from core.models import User

# Create your views here.
def signout(request):
    logout(request)
    return  redirect("home")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/includes/header.html',{
                'error': 'неверный догин или пароль'
            })
    return render(request, 'core/includes/header.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password  = request.POST.get('password')
        r_password = request.POST.get('repeat_password')
        if password != r_password:
            return  render(request, 'core/includes/header.html', {
                'error':  'пароли не совпадают'
            })
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        return redirect('home')
    
def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()
        return redirect('profile')
    return render(request, 'core/profile.html')