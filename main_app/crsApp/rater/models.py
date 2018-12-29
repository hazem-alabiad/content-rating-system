from django.db import models

class Book(models.Model):
	book_hash=models.CharField(max_length=100, unique=True)
	book_name=models.CharField(max_length=100)
	
	upload_date=models.DateTimeField()
	update_date=models.DateTimeField()

	ground_truth_label =models.CharField(max_length=10)
	predicted_label=models.CharField(max_length=10)
