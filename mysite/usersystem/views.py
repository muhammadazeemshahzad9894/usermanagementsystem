from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Clients
from django.contrib import auth
from django.contrib.auth.models import User
'''
def add_user(request, template_name='user_signup.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usersystem:manage_user')
    return render(request, template_name, {'form':form})


def manage_user(request, template_name='manage_user.html'):
    users = Clients.objects.all()
    data = {'user': users}
    #data[objects_list] = user_data
    return render(request, template_name, data)


def edit_user(request, pk, template_name='user_signup.html'):
    book = get_object_or_404(Clients, pk=pk)
    form = UserForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('usersystem:manage_user')


'''

def index(request):
    return render(request, 'index.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')

def userlogin(request):
    return render(request, 'userlogin.html')


def register(request):

    #return render(request, 'user_signup.html')
    return render(request, 'register_user.html')


def register_user(request):
    if request.method == 'POST':  # data sent by user
        data = Clients()
        data.firstname = request.POST.get('firstname', 'off')
        data.lastname=request.POST.get('lastname', 'off')
        data.cnic=request.POST.get('cnic', 'off')
        data.dob=request.POST.get('dob', 'off')
        data.age=request.POST.get('age', 'off')
        data.gender=request.POST.get('gender', 'off')
        data.password=request.POST.get('password', 'off')
        
        data.save()
        return redirect('usersystem:all_users')
    else:  # display empty form
        return render(request, 'register_user.html')
    

def all_users(request):
    users = Clients.objects.all()
    data = {'user': users}
    #data[objects_list] = user_data
    return render(request, 'all_users.html', data)


def delete_user(request, myid):

    instance = Clients.objects.get(id=myid)
    instance.delete()
    
    return redirect('usersystem:all_users')


def get_user(request, myid):

    user = Clients.objects.get(id=myid)
    data = {'user': user}
    return render(request, 'update_user.html', data)


def update_user(request, myid):

    if request.method == 'POST':  # data sent by user
        Clients.objects.filter(id=myid).update(firstname=request.POST.get('firstname', 'off'))
        Clients.objects.filter(id=myid).update(lastname=request.POST.get('lastname', 'off'))
        Clients.objects.filter(id=myid).update(cnic=request.POST.get('cnic', 'off'))
        #Clients.objects.filter(id=myid).update(dob=request.POST.get('dob', 'off'))
        Clients.objects.filter(id=myid).update(age=request.POST.get('age', 'off'))
        Clients.objects.filter(id=myid).update(gender=request.POST.get('gender', 'off'))
        Clients.objects.filter(id=myid).update(password=request.POST.get('password', 'off'))

        return redirect('usersystem:index')
    else:  # display empty form
        return HttpResponse("failed to update")


def approve_user(request, myid):

    Clients.objects.filter(id=myid).update(status=1)

    return redirect('usersystem:all_users')


def login_user(request):

    user = Clients.objects.filter(cnic=request.POST.get('login', 'off'), password=request.POST.get('password', 'off'), status=1)
    data = {'user':user}
    if user:
        return render(request, 'user_home.html', data)
    else:
        return HttpResponse('problem')


def login_admin(request):
    #password=request.POST.get('password', 'off')
    #username=request.POST.get('username', 'off')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            return redirect('usersystem:all_users')
        else:
            return HttpResponse('problem')
    

def logout_user(request):
    
    return redirect('usersystem:index')


def logout_admin(request):
    
    return redirect('usersystem:index')