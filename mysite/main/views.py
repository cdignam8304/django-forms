from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact
from .forms import Contact_Form
from .models import Contact
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from django.contrib import messages

# Create your views here.

def homepage(request):
    contacts = Contact.objects.all()
    return render(request=request,
                  template_name="main/homepage.html",
                  context={"contacts": contacts})


def new_contact(request):
    title = "New Contact"
    form = Contact_Form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        contact_name = f"{form.cleaned_data.get('first_name')} {form.cleaned_data.get('last_name')}"
        messages.success(request, f"New Contact Created: {contact_name}")
        form = Contact_Form()
    
    context = {
            "form": form,
            "title": title,
        }
    return render(request, "main/new_contact.html", context)


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


def edit_contacts(request):
    context = {}
    return render(request=request,
                  template_name="main/edit_contacts.html",
                  context=context)


