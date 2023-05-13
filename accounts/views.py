from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("product_list")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        try:
            user = User.objects.get(username=username)
            pass
        except User.DoesNotExist:
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)
            user.save()
            return redirect("login")

    return render(request, "accounts/register.html")


def logout_view(request):
    logout(request)
    return redirect("product_list")


@login_required(login_url="/accounts/login/")
def profile(request):
    user = request.user
    return render(request, "accounts/profile.html", {"user": user})
