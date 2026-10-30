
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactRequest


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactRequest

        fields = [
            'name',
            'email',
            'organization',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': _('Votre nom')
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': _('nom@entreprise.com')
                }
            ),

            'organization': forms.TextInput(
                attrs={
                    'placeholder': _('Votre organisation')
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'placeholder': _('Parlez-nous de votre projet'),
                    'rows': 5
                }
            ),
        }
