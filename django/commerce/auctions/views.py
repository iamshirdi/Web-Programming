from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.query_utils import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import User,auction,Categorys,bid,list_status, watch_list,comments

class NewForm(forms.Form):
    title = forms.CharField(label="Title")
    desc = forms.CharField(label="Description")
    url = forms.URLField(initial='http://',required=False)
    categ = forms.ModelChoiceField(queryset=Categorys.objects.all(),
            label ="Category")
    price =forms.DecimalField(label ="Price")
    



def index(request):
    return render(request, "auctions/index.html",{
        "lists":auction.objects.all()
    })

@login_required(login_url='/login')
def watch(request):
    if request.method=="POST":

        u = request.user.id
        a = int(request.POST.get('aid'))
        w= watch_list(article_id=a,user_id=u)
        w.save()
        return HttpResponseRedirect(reverse("watch"))

    #different articles_ids get for one user
    w = [i.article_id for i in watch_list.objects.filter(user_id=request.user.id)]
    return render(request, "auctions/watch.html",{
        "wl": [auction.objects.filter(pk=p) for p in w ]
    })

@login_required(login_url='/login')
def b_id(request):
    if request.method=="POST":
        a = int(request.POST.get('arid'))
        b = float(request.POST.get('bd'))
        bi = auction.objects.get(pk=a).price.id
        i = bid.objects.get(pk=bi)
        if i.bid_price < b:
            i.bid_price = b
            i.bid_user = request.user.username
            i.save()
            return HttpResponseRedirect(reverse("details",args=(a,)))
        else:
            return render(request, "auctions/detail.html",{
                "l":auction.objects.get(pk=a),
                "message":"Invalid Bid"
                })

@login_required(login_url='/login')
def close(request):
    if request.method == "POST":
        a = int(request.POST.get('arid'))
        s = auction.objects.get(pk=a)
        instance = list_status.objects.get(name="closed")
        s.status=instance
        s.save()
        return HttpResponseRedirect(reverse("details",args=(a,)))

@login_required(login_url='/login')
def del_watch(request):
    if request.method=="POST":
        id = int(request.POST.get('did'))
        instance = watch_list.objects.get(article_id=id)
        instance.delete()
        return HttpResponseRedirect(reverse("watch"))

@login_required(login_url='/login')
def com(request):
    if request.method=="POST":
        d= request.POST.get('descrip')
        u= request.POST.get('user_no')
        a =request.POST.get('article_no')
        c = comments.objects.create(comment=d,comment_user=u)
        ins = auction.objects.get(pk=a)
        ins.comment.add(c)
        return HttpResponseRedirect(reverse("details",args=(a,)))

#access through related name
def cat(request):
    if request.method=="POST":
        p= request.POST.get('test')
        print(p)
        c = Categorys.objects.get(cat=p)
        return render(request, "auctions/category.html",{
            "cats":c.categories.all(),
            "initial":Categorys.objects.all()})

    c = Categorys.objects.get(cat="Home")
    return render(request, "auctions/category.html",{
    "initial":Categorys.objects.all()})


def detail(request,list_id):
    return render(request, "auctions/detail.html",{
        "l":auction.objects.get(pk=list_id),
        "current":request.user.username ,
        "comments":auction.objects.get(pk=list_id).comment.all()   })

@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        # Check if form data is valid (server-side)
        form = NewForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            d = form.cleaned_data["desc"]
            ur = form.cleaned_data["url"]
            print("--------- ",form.cleaned_data["price"],request.user.username)
            
            #create inital object in bid table to reference back from article

            p = bid.objects.create(bid_price=form.cleaned_data["price"],bid_user =request.user.username)
            s = list_status.objects.get(name = "open")
           
            #get existing from user table 
            u =  User.objects.get(username=request.user.username)
           
           #when create the auction , you can add category 
           #after auction has been created otherwise you will encounter errors.
            auc = auction.objects.create(username = u, title = t, description =d, price =p, url =ur,status=s)
            auc.category.set([form.cleaned_data["categ"]])
            
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "auctions/create.html", {
                "form": form
            })
    return render(request,"auctions/create.html",{
        "form":NewForm()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")



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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
