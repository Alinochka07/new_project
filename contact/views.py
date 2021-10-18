from django.views.generic import CreateView

from .models import Contact, ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

