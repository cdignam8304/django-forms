from django import forms
from .models import Contact


class Contact_Form(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "city",
            "dob",
            "contact_type",
            "mktg_opt_in",
            "is_active",
            ]
