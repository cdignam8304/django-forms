from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact
from .forms import Contact_Form
from .models import Contact
from django.forms import formset_factory
from django.contrib import messages

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

# from hacksite for reference
# def register(request): # NB: The default request is a GET request
    
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid(): # check the form filled out correctly
#             user = form.save() # commit the new user record to the database
#             username = form.cleaned_data.get("username")
#             messages.success(request, f"New Account Created: {username}")
#             login(request=request, user=user) # so new user doesn't have to login again afer registering
#             messages.info(request, f"You are now logged in as: {username}")
#             return redirect("main:homepage") # arg using the variable names created in urls.py in main
#         else:
#             # Implement a short-term error handling solution:
#             for msg in form.error_messages: # form.error_messages is a dict
#                 # print(form.error_messages[msg]) # prints errors to console
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")

#     form = NewUserForm
#     return render(request=request, # This handles the default GET request
#                   template_name="main/register.html",
#                   context={"form": form})


