import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # products = Product.objects.all()
    products = Product.objects.filter(user=request.user)
    
    context = {
        'app_name' : 'Valorant Trade',
        'name': request.user.username,
        'npm' : '2306228390',
        'class': 'PBP F',
        'username': 'Furizou#9999',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        # form.save()
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    # Get product based on id
    product = Product.objects.get(pk=id)
    
    # Set product as the instance of form
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == "POST":
        # Save form & go back to home page (main)
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, 'edit_product.html', context)

def delete_product(request, id):
    # Get product based on id
    product = Product.objects.get(pk = id)
    
    # Detelete the product
    product.delete()
    
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response