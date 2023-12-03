from django.shortcuts import render
from . import forms

def login(req) :
    if req.method == 'POST' :
        form = forms.djangoForm(req.POST, req.FILES)
        if form.is_valid() :
            file = form.cleaned_data['image']
            with open('./form/upload/' + file.name, 'wb+') as destination :
                for chunk in file.chunks() :
                    destination.write(chunk)
            print(form.cleaned_data)
            # return render(req, 'form/login.html', {'form' : form }) render success Page
    # else :
    form = forms.djangoForm()
    return render(req, 'form/login.html', {'form' : form })




def register(req) :
    return render(req, 'form/register.html')
