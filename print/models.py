from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.name

class Document(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=100, default='')
	file = models.FileField(upload_to='Documents/%Y/%m/%d')
	color = models.CharField(max_length=100)
	bind = models.CharField(max_length=100, default='')
	pages = models.CharField(max_length=1000)
	copies = models.CharField(max_length=1000)
	building = models.CharField(max_length=500, default='')
	office = models.CharField(max_length=50, default='')
	suggestions = models.TextField(blank=True, null=True, default='None')
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

	def price_calc(self):
		pages = int(self.pages)
		copies = int(self.copies)
		color = int(self.color)
		bind = int(self.bind)

		return pages * copies + color + bind

	def total_price(self):
		pages = int(self.pages)
		copies = int(self.copies)
		color = int(self.color)
		bind = int(self.bind)

		return pages * copies + color + bind + 30

