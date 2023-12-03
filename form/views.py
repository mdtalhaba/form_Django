from django.shortcuts import render

def login(req) :
    return render(req, 'form/login.html')

def register(req) :
    return render(req, 'form/register.html')
