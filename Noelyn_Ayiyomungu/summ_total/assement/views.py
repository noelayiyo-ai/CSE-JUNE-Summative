from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render (request, 'intro.html')

def Register(request):
    if request.method == 'POST':
        data = request.POST
        form = RegistrationForm(data)
        if form.is_valid():
            form.save()
            messages.success(request,'Beneficiary Registered Successfullu')
            return redirect ('register')

    else:
        form = RegistrationForm()
    context = {
        'form':form
    }    
    return render (request,'registration.html', context)
        