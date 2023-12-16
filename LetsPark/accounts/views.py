from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        if User.objects.filter(user_id=request.POST['user_id']).exists():
            context['message'] = "아이디가 중복됩니다."
            return render(request, 'signup.html', context)
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            user_id=request.POST['user_id'], 
                                            password=request.POST['password1'],
                                            username=request.POST['username'],
                                            phone_number=request.POST['phone_number'],
                                            car_number=request.POST['car_number'],
                                            )
            user.save();
            auth.login(request, user)
            
            return redirect('/')
    return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request, 'accounts_home.html')
