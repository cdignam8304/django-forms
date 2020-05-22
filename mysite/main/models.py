from django.db import models
from django.utils import timezone

# Create your models here.


class ContactType(models.Model):
    
    contact_type = models.CharField(max_length=200)
    is_active = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name_plural = "Contact Types"
    
    def __str__(self):
        return self.contact_type


class Contact(models.Model):
    
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=200)
    dob = models.DateField(verbose_name="Date of Birth", default=timezone.now)
    contact_type = models.ForeignKey(ContactType,
                                    default=1,
                                    verbose_name="Contact Type",
                                    on_delete=models.SET_DEFAULT)    
    is_active = models.CharField(max_length=8, choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return f"/{self.email}/"
    
    
    
    
    
    
    