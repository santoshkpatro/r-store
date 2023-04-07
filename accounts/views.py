from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        print('Email: ', email)
        print('Password: ', password)
    return render(request, "accounts/login.html")

def register_view(request):
    return render(request, "accounts/register.html")