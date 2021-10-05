from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Lead(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.PositiveSmallIntegerField(default=0)
	picture = models.ImageField(default='default.jpg', upload_to='lead_pics/')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	converted = models.BooleanField(default=False)
	#assigned_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class User(AbstractUser):
	is_agent = models.BooleanField(default=False)

class Client(models.Model):
	converted_from = models.OneToOneField(Lead, on_delete=models.SET_NULL, null=True)
	agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)