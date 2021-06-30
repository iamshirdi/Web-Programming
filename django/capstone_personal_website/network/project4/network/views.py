from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import datetime

from .models import User, Profile, Skills

@login_required(login_url='/login') #redirect when user is not logged in
def index(request):
    u = request.user.username
    return HttpResponseRedirect(reverse("profile",args=(u,)))

def projects(request,name):
        if request.user.username == name:
            logged_in =True
        else:
            logged_in=False
        user_object = User.objects.get(username = name)
        profile_objects = Profile.objects.filter(profile_name = user_object)
        projects = profile_objects.filter(entity_type="projects")


        return render(request, "network/projects.html",{
            "user_logged_in":logged_in,
            "name":name,
             "projects":projects,

        })

def profile(request,name):

    user_object = User.objects.get(username = name)
    skill_objects = Skills.objects.filter(profile_name = user_object)
    profile_objects = Profile.objects.filter(profile_name = user_object)
    jobs = profile_objects.filter(entity_type="job")
    educations = profile_objects.filter(entity_type="education")
    if request.user.username == name:
        logged_in =True
    else:
        logged_in=False

    return render(request, "network/profile.html",{
        "user_logged_in":logged_in,
        "name":name,
        "skills":skill_objects,
        "jobs": jobs,
        "educations":educations
    })

@login_required(login_url='/login') #redirect when user is not logged in
def add_entity(request):
    if request.method == "POST":
        print(request.POST.get("start_date"))

        # only valid logged in user can use add button
        if not request.POST.get("logged_in")==request.user.username:
            return JsonResponse({"check": False}, status=200)
        entity = request.POST.get("entity")
        # # need to add condition like select but we can leave that for now
        entity_type = request.POST.get("entity_type")
        entity_desc = request.POST.get("entity_desc")
        start =request.POST.get("start_date")
        # start = datetime.datetime.strptime(sd, "%Y-%m-%d").strftime('%d/%m/%Y')
        end =request.POST.get("end_date")
        # end = datetime.datetime.strptime(ed, "%Y-%m-%d").strftime('%d/%m/%Y')
        uo = User.objects.get(username = request.user.username)
        p = Profile(profile_name = uo, entity = entity, entity_type = entity_type, entity_desc = entity_desc,start_date=start,end_date=end)
        p.save()
        if entity_type == "projects":
             u = request.user.username
             return HttpResponseRedirect(reverse("projects",args=(u,)))
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/login') #redirect when user is not logged in
def add_skills(request):
    if request.method == "POST":

        # only valid logged in user can use add button
        if not request.POST.get("logged_in") ==request.user.username:
            return JsonResponse({"check": False}, status=200)
        s = request.POST.get("skills")
        
        uo = User.objects.get(username = request.user.username)
        l = Skills.objects.filter(profile_name = uo)
        if len(l) > 0:
            l[0].skills = s
            l[0].save()
            #create if not exists else take first one
        else:
            p = Skills(profile_name = uo, skills = skills)
            p.save()
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/login') #redirect when user is not logged in
def del_entity(request):
    if request.method == "POST":

        # only valid logged in user can use add button
        if not request.POST.get("logged_in")==request.user.username:
            return JsonResponse({"check": False}, status=200)
        i = request.POST.get("del_id")
        
        d = Profile.objects.get(pk = i)
        d.delete()
        if d.entity_type == "projects":
             u = request.user.username
             return HttpResponseRedirect(reverse("projects",args=(u,)))
    return HttpResponseRedirect(reverse("index"))





def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
