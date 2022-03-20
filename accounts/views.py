from django.shortcuts import render
from django.contrib.auth.models import User  # 추가
from django.contrib import auth  # 추가
from django.shortcuts import redirect  # 추가


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            auth.login(request, user)
            return redirect('/posts')
    return render(request, 'accounts/signup.html')

def myinfo(request):
    if request.method == 'POST':
        user = request.user
        user.profile.college = request.POST['college']
        user.profile.major = request.POST['major']
        user.profile.save()
        return redirect('/posts')
    return render(request, 'accounts/myinfo.html')