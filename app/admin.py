from django.contrib import admin
from app.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','email','date')

admin.site.register(Blog,BlogAdmin)