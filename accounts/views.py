from django.shortcuts import render
from django.contrib.auth.models import User  # 추가
from django.contrib import auth  # 추가
from django.shortcuts import redirect  # 추가

def signup(request):
    # 추가
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/posts')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return redirect('blogPosts:index')
    return render(request, 'accounts/login.html')