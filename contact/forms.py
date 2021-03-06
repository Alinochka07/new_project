from django import forms
from .models import Contact
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """Форма подписки на email"""
    # captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваш email...", 'style':'max-width: 20em' 'justify-content:center'})
        }

        labels = {
            "email": ''
        }