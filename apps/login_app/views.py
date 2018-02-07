from django.shortcuts import render, HttpResponse, redirect

import bcrypt
from models import *
from django.contrib import messages

def index(request):
    return render(request,'login_app/index.html')#change folder name

def register(request):
    errors=User.objects.validator(request.POST)#sends the post info to validator in models
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        hashedpassword=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=hashedpassword)
        print user
        request.session['first_name']=user.first_name #logs this user into system
        return redirect('/')#change name

def login(request):
    login_return=User.objects.login_model(request.POST)
    if 'user' in login_return:
        request.session['id']=login_return['user'].id 
        request.session['first_name']=login_return['user'].first_name 
        request.session['admin'] = login_return['user'].admin
        if login_return['user'].admin==0:
            return redirect('user/user_portal')#change name
        elif login_return['user'].admin==1:
            return redirect('admin/admin_portal')#change name
    else:
        messages.error(request,login_return['error'])
        return redirect('/')

def logout(request):
    request.session.delete()
    return redirect('/')

# def display(request):
#     return render(request, "login_app/newpage.html")#add context if necessary #change folder name
