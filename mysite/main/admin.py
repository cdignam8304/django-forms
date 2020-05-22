from django.contrib import admin
from .models import Contact, ContactType, Generic, Schema

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactType)
admin.site.register(Generic)
admin.site.register(Schema)
