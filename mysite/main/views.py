from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact
from .forms import Contact_Form
from .models import Contact
from django.forms import formset_factory

# Create your views here.

def homepage(request):
    contacts = Contact.objects.all()
    return render(request=request,
                  template_name="main/homepage.html",
                  context={"contacts": contacts})


def new_contact(request):
    form = Contact_Form()
    return render(request=request,
                  template_name="main/new_contact.html",
                  context={"form": form})


def contacts(request):
    
    # For field headings in template
    contact_fields = [f.name for f in Contact._meta.get_fields()]
    contact_fields.remove("id")
    contact_fields.remove("last_updated")
    
    contacts = Contact.objects.all()
    data = []
    for contact in contacts:
        contact_dict = contact.__dict__
        # del contact_dict[""]
        del contact_dict["id"]
        data.append(contact_dict)
    ContactFormSet = formset_factory(Contact_Form, extra=0)
    formset = ContactFormSet(initial=data)
    
    return render(
        request=request,
        template_name="main/contacts.html",
        context={"formset": formset,
                 "contact_fields": contact_fields},
        )
    
