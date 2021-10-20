from django.views.generic import CreateView
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    def form_valid(self, form_class):
        messages.success(self.request, f'Ваш email успешно добавлен в нашу базу. Благодарим Вас за подписку!')
        return super().form_valid(form_class)

