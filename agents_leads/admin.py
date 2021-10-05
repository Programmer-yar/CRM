from django.contrib import admin
from . models import Lead, Client, User

admin.site.register(Lead)
admin.site.register(Client)
admin.site.register(User)