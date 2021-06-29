from django.contrib import admin
from .models import user
# Register your models here.
admin.site.register(user)
class user(admin.ModelAdmin):
    fields=("name","dob","email","phone ")
