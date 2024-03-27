from django.contrib import admin
from .models import *

# Register your models here.

# member model
admin.site.register(members)

# Book model
admin.site.register(Book)

# Transaction
# admin.site.register(transaction)

admin.site.register(Book_Issued)
