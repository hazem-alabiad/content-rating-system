from django.db import models
from rater.models import Book

class Feedbacks(models.Model):
	upload_date = models.DateTimeField()
	email = models.CharField(max_length=50)
	content = models.CharField(max_length=500)

	book = models.ForeignKey(Book, on_delete=models.CASCADE)
