from django.contrib import admin

# Register your models here.
from app.models import Book,Rating

admin.site.register(Book)
admin.site.register(Rating)