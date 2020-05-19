from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact
from .forms import Contact_Form

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
