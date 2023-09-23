from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib import messages


def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def createaccountpage(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        birthdate = request.POST['birthdate']
        bloodgroup = request.POST['bloodgroup']

        try:
            if password == repeatpassword:
                Patient.objects.create(name=name, email=email, gender=gender, phonenumber=phonenumber, address=address, birthdate=birthdate, bloodgroup=bloodgroup)
                user = User.objects.create_user(first_name=name, email=email, password=password, username=email)
                pat_group = Group.objects.get(name='patient')
                pat_group = Group.user_set.add(user)
                user.save()
                messages.success(request, 'Something went wrong.')
                return redirect('loginpage')
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
            messages.error(request, 'You have successfully signed up!')
    d = {'error': error}
    return render(request, 'createaccount.html',d)

def loginpage(request):
    return render(request, 'login.html')