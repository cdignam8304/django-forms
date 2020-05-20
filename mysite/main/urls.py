"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "main" # used for creating custom urls, so don't have to hard code urls

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("new_contact/", views.new_contact, name="new_contact"),
    path("contacts/", views.contacts, name="contacts"),
    path("edit_contacts/", views.edit_contacts, name="edit_contacts"),
]
