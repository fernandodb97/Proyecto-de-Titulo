from django.contrib import admin
from .models import General, Defensiva, Ofensiva, Distribucion
# Register your models here.

admin.site.register(General)

admin.site.register(Defensiva)

admin.site.register(Ofensiva)

admin.site.register(Distribucion)