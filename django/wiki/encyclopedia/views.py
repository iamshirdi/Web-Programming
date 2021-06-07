from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import re
from . import util
from django import forms
import random
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,name):
    e = "edit/"+name
    print("edit url generated is",e)
    markdowner = Markdown()
    u =util.get_entry(name) 

    if u == None:
        return render(request, "encyclopedia/error.html", {
            "error":"The requested page was not found"
            })

    marker =markdowner.convert(u)
    return render (request,"encyclopedia/title.html",{
        "title":name,
        "url": e,
        "content":marker
    })

def rand(request):
    tasks =util.list_entries()
    rando = random.randint(0,len(tasks)-1)
    print(rando)
    route = '/wiki/'+tasks[rando]
    return HttpResponseRedirect(route)

def edit(request,name):
    val = util.get_entry(name)

    class NewTaskForm(forms.Form):
        content = forms.CharField(label="New Content")
    print(name)
    if request.method == 'POST':
        print("post name is ",name)
        c =request.POST.get('content')
        util.save_entry(name,c)
        route = '/wiki/'+name
        print(route)
        return HttpResponseRedirect(route) 
    
    form = NewTaskForm(initial = {'content':val })
    return render(request, "encyclopedia/edit.html", {
        "form":form,
        "title":name
    })

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        route='wiki/'+query
        print(query)
        tasks = util.list_entries()
        if query in tasks:
            return HttpResponseRedirect(route)
        valid=[]
        rex = query.lower()
        print(tasks)
        for t in tasks:
            if re.search(rex,t.lower()):
                valid.append(t)

        print(valid)

        if len(valid)>0:
            return render(request, "encyclopedia/index.html", {
            "entries": valid})
        else:
            return render(request, "encyclopedia/error.html", {
            "error":"No valid tasks. Go back home for tasks"
            })
    return HttpResponse(f"this is not a valid get request")

def add(request):
# forms class for server update like invalid inputs
#  accepting instead of client only check
    class NewTaskForm(forms.Form):
        title = forms.CharField(label="New Title")
        text = forms.CharField(label="Text",max_length=800)

# Take in the data the user submitted and save it as form
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
# Check if form data is valid (server-side)
        if form.is_valid():
            #isolate from cleaned version of form data
            title = form.cleaned_data['title']
            content = form.cleaned_data['text']
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                "error":"Title name already exists"
                })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("add"))
        
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "add.html", {
                "form": form
            })
    return render(request, "encyclopedia/add.html", {
        "form":NewTaskForm()
    })