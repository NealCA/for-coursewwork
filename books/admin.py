from django.contrib import admin

# Register your models here.
from .models import Author, News

admin.site.register(Author)
admin.site.register(News)
