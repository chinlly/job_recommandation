from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
# def test(request):
#     user = Account(name="chinlly", pwd="123456")
#     user.save()
#     test_user = Account.objects.all()
#     return render(request, "test.html", {'user': test_user})
def indexPage(request):
    return render(request,'index.html')
def registerPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # if User.objects.filter(userame = username):
        #     messages.error(request, "username has already exists")

        if len(password) > 10 or len(password)<8:
            messages.error(request, "password must be under 10 and over 8 characters ")
            return redirect('register')

        user = User.objects.create_user(username = username, password = password)
        user.save()
        messages.success(request, "your Account has been created successfully")
        return redirect('login')
    return render(request, 'register.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:  # if it is authenticated
            login(request, user)
            return render(request, "index.html",{'username':username})
        else:
            messages.error(request, "you are not authenicated")
            return redirect('login')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request,"you have successfully logged out")
    return redirect('index')
