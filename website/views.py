from django.shortcuts import render

# Create your views here.
def index(request):
	return  render (request , 'chatbotmarket/index.html')	
def cart(request):
	return  render (request , 'chatbotmarket/cart.html')
def login(request):
	return render (request , 'chatbotmarket/login.html')
def account(request):
	return render (request , 'chatbotmarket/account.html')