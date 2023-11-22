from django.contrib import admin
from .models import Owner, Cat, Bird, Dog, Exotic_animal

admin.site.register([Owner, Cat, Bird, Dog, Exotic_animal])

# Register your models here.
