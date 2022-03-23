from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Nominee, DivTexts

admin.site.register(Nominee)
admin.site.register(DivTexts)