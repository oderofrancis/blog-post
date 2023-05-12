from django.contrib import admin
from app.models import Blog,Post

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','email','date')

admin.site.register(Blog,BlogAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','post','email','phone_number','date')

admin.site.register(Post,PostAdmin)