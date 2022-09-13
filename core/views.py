from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home_view(request):
        return render(request, "main.html", {})


def registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                        password=password)
        return render(request, 'login.html', {})
    return render(request, 'registration.html', {})


def logout_view(request):
    text = request.user.username
    logout(request)
    return HttpResponse(
        f"Вы не в системе, зарегистрируйтесь пожалуйста! {text}"
    )


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        login_ = request.POST.get('login','')
        pass_ = request.POST.get('pass','')
        print(pass_)
        user = authenticate(username=login_, password=pass_)
        if user is None:
            return redirect('/')
        else:
            login(request, user)
            return redirect('/action1/')
