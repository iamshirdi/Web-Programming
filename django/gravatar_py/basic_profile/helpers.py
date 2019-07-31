import hashlib
from django.http import JsonResponse


def encrypt(value):
    md5hash = hashlib.md5()
    md5hash.update(value.encode('utf-8'))
    encryptedHash = md5hash.hexdigest()
    return encryptedHash


def validateRequest(request):
    if(request.GET is None):
        response = JsonResponse({'status': '404', 'reason': 'route not found'})
        response.status_code = 404
        return response

    email = request.GET.get('userEmail')

    if email is None or not email.strip():
        response = JsonResponse({'status': '400', 'reason': 'invalid email'})
        response.status_code = 400
        return response


def validateResponse(response):
    if response.status_code == 200:
        return response.json()

    response = JsonResponse({'status': '404', 'reason': 'email not found'})
    response.status_code = 404
    return response
