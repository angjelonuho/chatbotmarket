from django import forms
from .models import w_QandA

class HomeForm(forms.Form):
	"""docstring for HomeForm"""
	post= forms.CharField(label='Your name', max_length=100)
