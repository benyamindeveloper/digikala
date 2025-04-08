from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import SignUpForm


def home(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    
    content = {
        'products': all_products,
        'categories': all_categories,
    }

    return render(request, 'index.html', content)


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def signup_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have signed up and logged in successfully.')
                return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def product(request,pk):
    product = Product.objects.get(id=pk)
    
    content = {
      'product': product
    }

    return render(request, 'product.html', content)
