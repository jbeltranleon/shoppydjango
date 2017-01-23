from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/registered')

        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {})

def registered(request):
    return render(request, 'registered.html', {})