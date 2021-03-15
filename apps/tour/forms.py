from django import forms
from django.forms import widgets

from apps.tour.models import Boot, Guide


class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Boot
        fields = '__all__'
