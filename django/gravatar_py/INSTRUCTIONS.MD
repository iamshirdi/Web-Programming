What is garavtar:
A service linking an email to an avatar that can be globally used by other services.

1. https://en.gravatar.com/
2. https://en.gravatar.com/site/implement/images/
3. https://en.gravatar.com/site/implement/profiles/json/

Detail: '.../images/{md5Hash}' - https://en.gravatar.com/site/implement/hash/

Blank project:
django-admin.py startproject my-app

> - pip install django
> - pip install requests
> - pip install hashlib

python manage.py runserver

Considering that our project has two routes:

> - /profile
> - /profile/json

And the _/profile/json_ use query parameters to get the _userEmail_ filter value

Instructions:

1. Create a component that takes one property: _email_ and displays that user's gravatar.

2. Now also display the username coming from the profile beneath the image. Remember to put in correct error handling!

3. Now make you component dynamic. Create a text-field, where the user of you app can input any email, and their corresponding gravatar will be displayed.
   And if you have time, retain all gravatars the user has previously displayed.
