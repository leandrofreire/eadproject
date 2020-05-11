from django.contrib import admin

from .models import User, Professor

admin.site.register(User)
admin.site.register(Professor)