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
    
    
    
    
class Schema(models.Model):
    schema_name = models.CharField("schema name", max_length=200, blank=False)
    string1 = models.CharField("string1", max_length=200, blank=False)
    string2 = models.CharField("string2", max_length=200, blank=True)
    string3 = models.CharField("string3", max_length=200, blank=True)
    string4 = models.CharField("string4", max_length=200, blank=True)
    string5 = models.CharField("string5", max_length=200, blank=True)
    date1 = models.CharField("date1", max_length=200, blank=True)
    date2 = models.CharField("date2", max_length=200, blank=True)
    date3 = models.CharField("date3", max_length=200, blank=True)
    amount1 = models.CharField("amount1", max_length=200, blank=True)
    amount2 = models.CharField("amount2", max_length=200, blank=True)
    
    class Meta():
        verbose_name_plural = "Schemas"
        
    def __str__(self):
        return self.schema_name
    
    

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
    
    schema_name = models.ForeignKey(Schema,
                                    default=None,
                                    verbose_name="schema name",
                                    on_delete=models.SET_DEFAULT)
    string1 = models.CharField("string1", max_length=200, blank=False)
    string2 = models.CharField("string2", max_length=200, blank=True)
    string3 = models.CharField("string3", max_length=200, blank=True)
    string4 = models.CharField("string4", max_length=200, blank=True)
    string5 = models.CharField("string5", max_length=200, blank=True)
    date1 = models.DateField("date1", default=None, blank=True, null=True)
    date2 = models.DateField("date2", default=None, blank=True, null=True)
    date3 = models.DateField("date3", default=None, blank=True, null=True)
    amount1 = models.DecimalField("amount1", decimal_places=2, max_digits=10, blank=True, null=True)
    amount2 = models.DecimalField("amount2", decimal_places=2, max_digits=10, blank=True, null=True)
    status = models.CharField("status", max_length=10, choices=STATUS, default=OPEN)
    created_at = models.DateTimeField("created", auto_now_add=True)
    last_updated = models.DateTimeField("updated", auto_now=True)
    
    
    class Meta():
        verbose_name_plural = "Generic Datasets"
    
    def __str__(self):
        return f"{self.schema_name}: {self.string1}"