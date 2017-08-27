from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *





# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    print result

    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/dashboard')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/dashboard')

def dashboard(request):

    context={
        'user': User.objects.get(id=request.session['user_id']),
        'wished_items': User.objects.get(id=request.session['user_id']).wishing.all(),
        'all_items': Item.objects.exclude(added_by_id=request.session['user_id'])
    }
     
    return render(request, 'login/dashboard.html', context)

def add(request):
    print request.session['user_id']
    return render(request, 'login/add.html')

def add_item(request):

    Item.objects.create(name=request.POST['item'], added_by_id=request.session['user_id'] )
    Item.objects.get(name = request.POST['item']).wished_by.add(User.objects.get(id=request.session['user_id']))
    
    return redirect('/dashboard')

def add_wishlist(request, item_id):

    Item.objects.get(id=item_id).wished_by.add(User.objects.get(id=request.session['user_id']))

    return redirect('/dashboard')


def remove(request, item_id):
    Item.objects.get(id=item_id).wished_by.remove(User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')

def delete(request, item_id):

    Item.objects.get(id=item_id).delete()

    return redirect('/dashboard')

def description(request, item_id):
    context={
        'users':Item.objects.get(id=item_id).wished_by.all(),
        'item': Item.objects.get(id=item_id)
    }
    return render(request, 'login/description.html', context)