from django.contrib import admin
from .models import ContactRequest
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display=('name','email','organization','created_at')
    search_fields=('name','email','organization')
    readonly_fields=('created_at',)
