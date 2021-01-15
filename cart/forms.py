from django import forms
from print.models import *


class PrinterApplication(forms.ModelForm):
    class Meta:
        model = PrinterSchedule
        fields = ('to_perform', 'description')

        widgets = {
            'to_perform': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
