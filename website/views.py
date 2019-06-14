from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import HomeForm

# Create your views here.
def index(request):
	return  render (request , 'chatbotmarket/index.html')	
def cart(request):
	return  render (request , 'chatbotmarket/cart.html')
def login(request):
	return render (request , 'chatbotmarket/login.html')
def account(request):
	return render (request , 'chatbotmarket/account.html')
def support(request):
    return render (request , 'chatbotmarket/support.html')
def fanmarket(request):
    return render (request , 'fanmarket/fanmarket.html')






		