from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from website.forms import SignUpForm


# Create your views here.
def index(request):
	return  render (request , 'chatbotmarket/index.html')	
def cart(request):
	return  render (request , 'chatbotmarket/cart.html')

def auth_login(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'chatbotmarket/login.html', {'form': form})

def account(request):
	return render (request , 'chatbotmarket/account.html')
def support(request):
    return render (request , 'chatbotmarket/support.html')
def fanmarket(request):
    return render (request , 'fanmarket/fanmarket.html')








		