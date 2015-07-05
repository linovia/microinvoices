from django.contrib import admin
from . import models


class InvoiceAdmin(admin.ModelAdmin):
    fields = [
        'name', 'additional_infos', 'owner',
    ]

admin.site.register(models.Invoice, InvoiceAdmin)
