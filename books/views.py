from django.shortcuts import render_to_response,get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from books.models import Author

from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication

from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib import auth


# login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')

        if name:
            try:
                user = Author.objects.get(username=name)
            except:
                payload = {'sorry': 'invalid username !\n'}
                http_badresponse = HttpResponse(json.dumps(payload))
                http_badresponse['content-type'] = 'text/plain'
                http_badresponse.status_code = 404
                http_badresponse.reason_phrase = 'wrong username \n'
                return http_badresponse

        else:
            return HttpResponse("please enter your username and password\n")

        if pwd:
            # get pwd

            if user.password == pwd :
                request.session['name'] = user.username
                # 登陆成功
                payload = {'Hello': 'welcome!'}
                http_response = HttpResponse(json.dumps(payload))
                http_response['content-type'] = 'text/plain'
                http_response.status_code = 200
                http_response.reason_phrase = 'OK'
                return http_response
            else:
                # 登陆失败
                payload = {'sorry': 'password is wrong !'}
                http_badresponse = HttpResponse(json.dumps(payload))
                http_badresponse['content-type'] = 'text/plain'
                http_badresponse.status_code = 404
                http_badresponse.reason_phrase = ' password is wrong'
                return http_badresponse
        else:
            return HttpResponse("please enter your username and password")


    # post request
    else:
        payload = {'request problem': 'need POST request '}
        http_badresponse = HttpResponse(json.dumps(payload))
        http_badresponse['content-type'] = 'text/plain'
        http_badresponse.status_code = 404
        http_badresponse.reason_phrase = 'need POST request'
        return http_badresponse

# log out


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        # 登出成功 (ok)
        del request.session['name']
        payload = {'Goodbye': 'see u next time !'}
        http_response = HttpResponse(json.dumps(payload))
        http_response['content-type'] = 'text/plain'
        http_response.status_code = 200
        http_response.reason_phrase = 'OK'
        return http_response
    else:
        # 登出失败 (ok)
        payload = {'request problem': ' need POST request '}
        http_badresponse = HttpResponse(json.dumps(payload))
        http_badresponse['content-type'] = 'text/plain'
        http_badresponse.status_code = 404
        http_badresponse.reason_phrase = 'need POST request'
        return http_badresponse


