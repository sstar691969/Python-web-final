from django.contrib import admin
from .models import Movie,Showing,Customer,Ticket
# Register your models here.

admin.site.register(Movie)
admin.site.register(Showing)
admin.site.register(Customer)
admin.site.register(Ticket)


