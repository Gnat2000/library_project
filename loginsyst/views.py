from django.contrib import auth
from django.shortcuts import render_to_response, redirect, render
from django.template.context_processors import csrf

from loginsyst.forms import UserCreateForm
from django.utils.timezone import now
import datetime


def index(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['today'] = datetime.date.today()
    args['now'] = now()
    return render_to_response("backend/index.html", args)


def home_files(request, filename):
    return render_to_response(filename, content_type="text/plain")


def login(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('registration/login.html', args)
    else:
        return render_to_response('registration/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = UserCreateForm()
    if request.POST:
        newuser_form = UserCreateForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'],
                                        email=newuser_form.cleaned_data['email']),
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration/register.html', args)
