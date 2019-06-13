from django.contrib import admin
from testapp.models import book
# Register your models here.

class bookadmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']

admin.site.register(book,bookadmin)
#now apply 'py manage.py makemigrations' and then migrate then createsuperuser commands on cmd.
#and then finally 'py manage.py runserver'
#then add 4 to 5 entries in the created table book.
