from django.db import models

class w_QandA(models.Model):
	website_question = models.CharField(max_length=500)
	website_answer = models.CharField(max_length=500) 