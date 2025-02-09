from django.contrib import admin
from .models import Recipient

class RecipientAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'comment']
    search_fields = ['name', 'email']

admin.site.register(Recipient, RecipientAdmin)

