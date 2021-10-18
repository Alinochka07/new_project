from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView
from .forms import *
from .models import Token



def login_view(request):

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('mainapp:product-list')
        else:
            context['has_error'] = True

    return render(request, 'login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('mainapp:product-list')


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration.html', context={'form': form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                is_active=True
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('account:login')
        return render(request, 'registration.html', context={'form': form})


def user_activate_view(request, token):
    token = get_object_or_404(Token, token=token)
    user = token.user
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('mainapp:product-detail')



