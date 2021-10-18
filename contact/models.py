from django.db import models
from django.forms import ModelForm


class Contact(models.Model):
    """Подписка на email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class ContactForm(ModelForm):
    """Форма подписки на email"""
    # captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ['email',]
       
