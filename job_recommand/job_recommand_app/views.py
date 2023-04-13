from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
import requests
import pandas as pd
import ast
import ast
import numpy as np


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
    user = get_user(request)
    print(user)
    profile_exist = Profile.objects.filter(name=user).exists()
    if profile_exist == False:
        jobs = "software"
    else:
        profile = Profile.objects.get(name=user)
        df = pd.read_csv("linkedin.csv")
        df = df.drop(axis=1, columns=["linkedin","profile_picture","description","Experience","Name","skills","location"])
        df = df.dropna()
        user_input = profile.skills
        print("User Skills:",user_input)
        df['similarity'] = df['clean_skills'].apply(lambda x: jaccard_similarity(set(ast.literal_eval(x)),set(user_input)))
        N = 1
        # print(df['similarity'])
        recommended_jobs = df.nlargest(N, 'similarity')
        # print(recommended_jobs['index'],recommended_jobs['category'],recommended_jobs['position'])
        # print(recommended_jobs['category'].iloc[0])
        jobs = recommended_jobs['category'].iloc[0]
        user = get_user(request)
        print(jobs)
        profile = Profile.objects.get(name=user)
        profile.keyword = jobs
        profile.save()
    params = {
        "app_id": "ad594a9d",
        "app_key": "740a7e78f8f00020c045cd46e59d6932",
        "what": jobs,
        "results_per_page": 10,
        "content-type": "application/json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data['results']

    job_listings = []
    for result in results:
        job = {"title": result['title'], "location": result['location']['area'],
               "company": result['company']['display_name'], "url": result['redirect_url'],
               "description": result['description']}
        job_listings.append(job)

    # print(job_listings)

    return render(request, 'home.html', {'job_listings': job_listings})


def indexPage(request):
    return render(request, 'login.html')


def registerPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # if User.objects.filter(userame = username):
        #     messages.error(request, "username has already exists")

        if len(password) > 10 or len(password) < 8:
            messages.error(request, "password must be under 10 and over 8 characters ")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username is already taken.'})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "your Account has been created successfully")
        authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'profile.html')
        # return redirect("home")

    return render(request, 'register.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:  # if it is authenticated
            login(request, user)
            print(request.method)

            # return render(request, "index.html", {'username': username})
            return redirect('home')
        else:
            messages.error(request, "you are not authenicated")
            return render(request, 'index.html', {'username': username})

    return render(request, 'login.html')


def signout(request):
    logout(request)
    messages.success(request, "you have successfully logged out")
    return redirect('login')


def profile(request):
    if request.method == "POST":
        user = get_user(request)
        profile_exist = Profile.objects.filter(name=user).exists()
        if profile_exist == False:
            profile = Profile(name=user, skills=request.POST["list"])

        else:
            profile = Profile.objects.get(name=user)
            profile.skills = request.POST["list"]
        profile.save()

        print(request.POST)
        print("1s")

        # form = ProfileForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # return render(request, "profile.html", {"form": form})
        return redirect('home')
    else:
        print('get')
    return render(request, "profile.html")



def jaccard_similarity(set1: set, set2: set) -> float:
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)