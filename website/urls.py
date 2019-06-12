from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('cart' , views.cart , name = 'cart'),
    path('login' , views.login , name = 'login'),
    path('account' , views.account , name = 'account'),

    path('fanmarket/', views.fanmarket, name = 'fanmarket')
]