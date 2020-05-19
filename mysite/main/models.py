from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=200)
    dob = models.DateField(verbose_name="Date of Birth", default=datetime.now())
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(null=False, default=True)
    
    class Meta():
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return f"/{self.email}/"