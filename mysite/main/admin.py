from django.contrib import admin
from .models import Contact, ContactType

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactType)