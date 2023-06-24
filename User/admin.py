from django.contrib import admin
from .models import User, Clients, University

# Register your models here.
admin.site.register(User)
admin.site.register(Clients)
admin.site.register(University)