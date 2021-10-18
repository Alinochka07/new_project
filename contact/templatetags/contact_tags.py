from django import template
from contact.models import ContactForm

register = template.Library()



@register.inclusion_tag("contact_form.html")
def contact_form():
    return {"contact_form": ContactForm()}

