from django.db import models

class Feedback(models.Model):
	date = models.DateTimeField()
	email = models.CharField(max_length=50)
	content = models.CharField(max_length=500)

