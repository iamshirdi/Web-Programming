from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from . import helpers
import requests
from hashlib import md5

def userJson(request):

    email = "alanbueno8@gmail.com"

    # encryption: use the encrypt function from the helpers

    # https://en.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50

    # https://en.gravatar.com/205e460b479e2e5b48aec07710c08d50.json

    # request library usage: requests.get({route}) and use the function .json() to parse of the response

    hashed = md5(email.encode()).hexdigest()
    email_url = 'https://en.gravatar.com/' + hashed + '.json'
    info = requests.get(email_url).json()
    grav_url=info['entry'][0]['photos'][0]['value']

    return JsonResponse(info)


def user(request):
    if request.method == 'GET':
        return render(request,'profile/forms.html')

    elif request.method == 'POST':
        email=request.POST.get("your_email")
    # current_email='htanmsa@gmail.com'
        hashed = md5(email.encode()).hexdigest()
        email_url = 'https://en.gravatar.com/' + hashed + '.json'
        info = requests.get(email_url).json()
        grav_url=info['entry'][0]['photos'][0]['value']+'?s=500'
        dn=info['entry'][0]['displayName']
        pu=info['entry'][0]['preferredUsername']

        # return HttpResponse(grav_url)
        return render(request,'profile/index.html',{'var1':grav_url ,'var2':dn,'var3':pu})



    # return HttpResponse(current_email)
