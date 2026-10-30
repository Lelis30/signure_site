
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import ContactForm


def home(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        contact = form.save()

        subject = f"SIGNURE - Nouvelle demande de {contact.name}"

        body = (
            f"Nouvelle demande de contact SIGNURE\n\n"
            f"Nom : {contact.name}\n"
            f"Email : {contact.email}\n"
            f"Organisation : {contact.organization}\n\n"
            f"Message :\n{contact.message}\n"
        )

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_NOTIFICATION_EMAIL],
            reply_to=[contact.email],
        )
        print("SMTP HOST :", settings.EMAIL_HOST)
        print("SMTP LOGIN PRESENT :", bool(settings.EMAIL_HOST_USER))
        print("SMTP KEY PRESENT :", bool(settings.EMAIL_HOST_PASSWORD))

        try:
            email.send(fail_silently=False)

        except Exception as e:
            print("ERREUR EMAIL SIGNURE :", type(e).__name__, str(e))

            messages.warning(
                request,
                "Votre demande a été enregistrée. "
                "La notification par e-mail n'a pas pu être envoyée."
            )

        else:
            messages.success(
                request,
                "Votre message a bien été reçu. "
                "Merci de votre intérêt pour SIGNURE."
            )

        return redirect('/#contact')

    return render(request, 'core/home.html', {'form': form})


def apropos(request):
    return render(request, 'core/apropos.html')


def expertises(request):
    return render(request, 'core/expertises.html')


def approche(request):
    return render(request, 'core/approche.html')

def implantations(request):
    return render(request, "core/implantations.html")