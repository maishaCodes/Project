from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .form import RegistrationForm


def register(request):
    
    if request.method == "POST":
        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("add-items")
        
        messages.error(request, "error user creation")
        return redirect("add-items")
      
       
    
    else:
        
        form = RegistrationForm()
        context = {
            "form": form
        }
    
        return render(request, "registration.html", context)