from django.contrib import admin
from .models import Contact, ContactType, Generic

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactType)
admin.site.register(Generic)
