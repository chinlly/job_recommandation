from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm
import requests

# Create your views here.
# def test(request):
#     user = Account(name="chinlly", pwd="123456")
#     user.save()
#     test_user = Account.objects.all()
#     return render(request, "test.html", {'user': test_user})

# def indexPage(request):
#     return render(request,'index.html')


def homePage(request):

    url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

    params = {
        "app_id": "ad594a9d",
        "app_key": "740a7e78f8f00020c045cd46e59d6932",
        "what": "software",
        "results_per_page": 2,
        "content-type": "application/json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data['results']


    job_listings = []
    for result in results:
        job = {"title": result['title'], "location": result['location']['area'],
               "company": result['company']['display_name'], "url": result['redirect_url'],
               "description":result['description']}
        job_listings.append(job)




    return render(request, 'home.html', {'job_listings': job_listings})


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


def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        # return render(request,"post/new.html",{"form":form} )
    else:
        form = ProfileForm()
    return render(request,"profile.html",{"form":form} )