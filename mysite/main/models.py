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
    
    IN = "IN"
    OUT = "OUT"
    INOUT = [
        (IN, "In"),
        (OUT, "Out"),
    ]
    
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField("last name", max_length=200)
    email = models.EmailField("email", max_length=200)
    city = models.CharField("city", max_length=200)
    dob = models.DateField("d.o.b.", default=timezone.now)
    contact_type = models.ForeignKey(ContactType,
                                    default=1,
                                    verbose_name="contact type",
                                    on_delete=models.SET_DEFAULT)
    mktg_opt_in = models.CharField("opt in", max_length=3, choices=INOUT, default=IN)
    is_active = models.CharField("active", max_length=8, choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField("created", auto_now_add=True)
    last_updated = models.DateTimeField("updated", auto_now=True)
    
    class Meta():
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return f"/{self.email}/"
    
    
    
class Generic(models.Model):
    
    OPEN = 'OPEN'
    ACCEPTED = 'ACCEPTED'
    REJECTED = "REJECTED"
    DEFERRED = "DEFERRED"
    ESCALATED = "ESCALATED"
    
    STATUS = [
        (OPEN, 'Open'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (DEFERRED, 'Deferred'),
        (ESCALATED, 'Escalated')
    ]
    
    data_type = models.CharField("data type", max_length=200)
    string1 = models.CharField("string1", max_length=200)
    string2 = models.CharField("string2", max_length=200)
    string3 = models.CharField("string3", max_length=200)
    string4 = models.CharField("string4", max_length=200)
    string5 = models.CharField("string5", max_length=200)
    date1 = models.DateField("date1", default=timezone.now)
    date2 = models.DateField("date2", default=timezone.now)
    date3 = models.DateField("date3", default=timezone.now)
    status = models.CharField("status", max_length=10, choices=STATUS, default=OPEN)
    created_at = models.DateTimeField("created", auto_now_add=True)
    last_updated = models.DateTimeField("updated", auto_now=True)
    
    
    class Meta():
        verbose_name_plural = "Generic Datasets"
    
    def __str__(self):
        return f"{self.data_type}: {self.id}"
    
    
class Schema(models.Model):
    schema_name = models.CharField("string1", max_length=200)
    string1 = models.CharField("string1", max_length=200)
    string2 = models.CharField("string2", max_length=200)
    string3 = models.CharField("string3", max_length=200)
    string4 = models.CharField("string4", max_length=200)
    string5 = models.CharField("string5", max_length=200)
    date1 = models.DateField("date1", default=timezone.now)
    date2 = models.DateField("date2", default=timezone.now)
    date3 = models.DateField("date3", default=timezone.now)
    
    class Meta():
        verbose_name_plural = "Schemas"
        
    def __str__(self):
        return self.schema_name
    