from django.contrib import admin

from .models import Boot, Voyage, Guide

# Register your models here.


admin.site.register((Boot, Voyage, Guide))
