#from dbm.ndbm import library
from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from .models import Library
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from library.forms import LibraryForm,SignUpForm,LoginForm
from django.contrib.auth.models import Group

# Create your views here.

#this is our home section
def home(request):
    
    

      bks =Library.objects.all()  
      return render(request,'core/home.html',{'books':bks})

#this function update and edit

def Update(request,id):
    if request.method=='POST':
        pi = Library.objects.get(pk=id)
        fm= LibraryForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Library.objects.get(pk=id)
        fm= LibraryForm(instance=pi)
                
    return render(request,'core/update.html',{'form':fm})



#this function will delete

def delete(request,id):
    if request.method == 'POST':
        pi = Library.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')




#signup
def user_signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! you become a Member')
            form.save()
    else:        
     form =SignUpForm()
    return render(request,'core/signup.html',{'form':form})   

def List(request):
    if request.method == 'POST':
        fm= LibraryForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = LibraryForm()  
    return render(request,'core/list.html',{'form':fm})



def user_login(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully.')
                    return HttpResponseRedirect('/list/')
        else:            
            form=LoginForm()
        return render(request,'core/login.html', {'form':form})

    else:
        return HttpResponseRedirect('/list/')  



#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')            



        

         
