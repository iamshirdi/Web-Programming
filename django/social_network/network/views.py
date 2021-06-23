from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator

from .models import User, Posts, follow_db



class NewPostForm(forms.Form):
    new_post = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 4}),
        label="New Post", max_length=1000)


def edit_like(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("id")
        p = Posts.objects.get(pk=int(post_id))
        u = User.objects.get(username=request.user.username)
        l = p.liked_users.all()
        if not u in l:
            p.liked_users.add(u)
            d = Posts.objects.get(pk=int(post_id))
            return JsonResponse({
                "changed": d.liked_users.all().count(),
                "added":bool(1)
                    }, status=200)
        else:
            p.liked_users.remove(u)
            d = Posts.objects.get(pk=int(post_id))
            return JsonResponse({
                "changed": d.liked_users.all().count(),
                "added":bool(0)
            }, status=200)



def index(request):
    posts = Posts.objects.all().order_by('-time')
    ## pagination add
    nxt =bool(0)
    prev =bool(0)
    objects = Paginator(posts, 10)
    num_pages =objects.num_pages
    try:
        page = int(request.GET.get("page"))
        lst = objects.page(page)
        if lst.has_previous():
            prev = bool(1)
        #next, prev check
        if lst.has_next():
            nxt = bool(1)
        p = lst.object_list
    except:
        lst = objects.page(1)
        p = lst.object_list
        if lst.has_next():
            nxt = bool (1)
        pass
    
    return render(request, "network/index.html", {
        "form": NewPostForm(),
        "posts":p,
        "next":nxt,
        "previous":prev
        })

# @csrf_exempt
def edit_post(request):
    if request.method == "POST":
        check = json.loads(request.body)
        post_id = check.get("id")
        text = check.get("post")
        print("post id and text are",post_id,text)
        p = Posts.objects.get(pk=int(post_id))
        print(p,p.name,request.user.username,p.post)
        if request.user.username == p.name:
            print("in loop")
            p.post = text
            p.save()
            d = Posts.objects.get(pk=int(post_id))
            return JsonResponse({
                "changed": d.post
                    }, status=200)
        else:
            return JsonResponse({
                "error": f"Not valid User."
            }, status=400)


@csrf_exempt
def follow_view(request,name):
    if request.method == "POST":
        check = json.loads(request.body)
        c = check.get("data")
        print("c is",c)
        #remove follower
        if c == "True":
            user_object = User.objects.get(username = name)
            f = follow_db.objects.get(name = user_object)
            u = User.objects.get(username = request.user.username)
            print(user_object,u,f.followers.all())
            f.followers.remove(u)
            return JsonResponse({
            "changed": "False"
                }, status=200)

        #if c is false not follower add it
        if c == "False":
            #created post user object
            user_object = User.objects.get(username = name)
            # the current user who wants is gonna follow the created post object
            f = follow_db.objects.get(name = user_object)
            u = User.objects.get(username = request.user.username)
            f.followers.add(u)
            return JsonResponse({
            "changed": "True"
                }, status=200)

        
    #get request to check if current user is already follower
    u = User.objects.get(username = name)
    f1 = follow_db.objects.get(name = u)
    f2 = f1.followers.all()
    fc = "False"
    for i in f2:
        x= str(i)
        y= request.user.username
        print("nameeee",x,y,type(x),type(y))
        if x == y:
            fc = "True"
    return JsonResponse({"check": fc}, status=200)

def add(request):
    if request.method == "POST":
        form =NewPostForm(request.POST)
        if form.is_valid():
            pst = form.cleaned_data["new_post"]
            p = Posts(post = pst , name = request.user.username)
            p.save()
            #Add user to start follower database
            user_object = User.objects.get(username =request.user.username)

            #check follower db when creating post otherwise add
            try:
                follow_db.objects.get(name=user_object)
                pass
            except ObjectDoesNotExist:
                f = follow_db(name=user_object)
                f.save()
            return HttpResponseRedirect(reverse("index"))
        else:
        # If the form is invalid, re-render the page with existing information.
            return render(request, "network/add.html", {
                "form": form
            })
    return HttpResponseRedirect(reverse("index"))

@login_required(login_url='/login')
def profile_view(request,name):
    #check if viewing user own profile 
    if name == request.user.username:
        ad = "False"
    else:
        ad = "True"
    posts = Posts.objects.filter(name = name).order_by('-time')
    u = User.objects.get(username=name)
    f1 = follow_db.objects.get(name = u)
    f2 = u.following.all()

    #check if already follower
    fc = "False"
    for i in f1.followers.all():
        x= str(i)
        y= request.user.username
        print("nameeee",x,y,type(x),type(y))
        if x == y:
            fc = "True"
            print("fc isssss",fc)

#can try filter instead of above method
# print("testtttttttttttttt",u.following.all())

   ## pagination add
    nxt =bool(0)
    prev =bool(0)
    objects = Paginator(posts, 10)
    num_pages =objects.num_pages
    try:
        page = int(request.GET.get("page"))
        lst = objects.page(page)
        if lst.has_previous():
            prev = bool(1)
        #next, prev check
        if lst.has_next():
            nxt = bool(1)
        p = lst.object_list
    except:
        lst = objects.page(1)
        p = lst.object_list
        if lst.has_next():
            nxt = bool (1)
        pass
    
    print(u,f1,f2)
    print("is it a follow check",ad,fc)
    return render(request, "network/profile.html", {
    "posts":p,
    "n":name,
    "followersx":f1.followers.all(),
    "followingx":f2,
    "c1":f1.followers.all().count(),
    "c2":f2.count(),
    "ad":ad,
    "follow_check":fc,
    "next":nxt,
    "previous":prev,
    })



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

@login_required(login_url='/login')
def following_view(request):
    u = User.objects.get(username=request.user.username)
    print("u is ",u)
    fg = u.following.all()
   

    #following users
    f = []
    for i in fg:
        f.append(i.name)
    #following users posts get
    posts = Posts.objects.filter(name__in = f).order_by('-time')

    ## pagination add
    nxt =bool(0)
    prev =bool(0)
    objects = Paginator(posts, 10)
    num_pages =objects.num_pages
    try:
        page = int(request.GET.get("page"))
        lst = objects.page(page)
        if lst.has_previous():
            prev = bool(1)
        #next, prev check
        if lst.has_next():
            nxt = bool(1)
        p = lst.object_list
    except:
        lst = objects.page(1)
        p = lst.object_list
        if lst.has_next():
            nxt = bool (1)
        pass
    


    return render(request, "network/following.html",{
        "posts":p,
        "next":nxt,
        "previous":prev
    })

