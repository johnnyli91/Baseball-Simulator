from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Team, Player


def index(request):
    if request.user.is_authenticated():
        user_team = Team.objects.filter(user=request.user)
        user_player = Player.objects.filter(team__in=user_team)
        return render(request, '../static/index.html', {'user_team':user_team, 'user_player':user_player})
    else:
        return render(request, '../static/app/views/registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../static/index.html')
    else:
        form = UserCreationForm()
    return render(request, '../static/app/views/signup.html', {'form':form})

def roster(request):
    if request.user.is_authenticated():
        user_team = Team.objects.filter(user=request.user)
        user_player = Player.objects.filter(team__in=user_team)
        return render(request, '../static/app/views/roster.html', {'user_team':user_team, 'user_player':user_player})
    else:
        return render(request, '../static/app/views/registration/login.html')

