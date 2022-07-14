from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth import authenticate

# Create your views here.

# def user_registration(request):
#     form = RegistrationForm()
#     context={
#         'form': form
#     }
#     if request.method=="POST":
#         form=RegistrationForm(request.post)
#         if form.is_valid()
            
        
        
        
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')