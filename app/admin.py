from django.contrib import admin
from .models import Client, Intervenant, Intervention

# Register your models here.

admin.site.register(Client)
admin.site.register(Intervenant)
admin.site.register(Intervention)