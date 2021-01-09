from django import forms
from print.models import Printer, PrinterSchedule, PrinterModel


class PrinterCreateForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'printerModel': forms.Select(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'cartridge': forms.Select(attrs={'class': 'form-control'}),
        }


class PrinterModelCreateForm(forms.ModelForm):
    class Meta:
        model = PrinterModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'firm': forms.Select(attrs={'class': 'form-control'}),
        }


class PrinterModelUpdateForm(forms.ModelForm):
    class Meta:
        model = PrinterModel
        fields = ('name', 'type', 'firm')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'firm': forms.Select(attrs={'class': 'form-control'}),
        }

# class PrinterScheduleCreateForm(forms.ModelForm):
#     class Meta:
#         model = PrinterSchedule
#         fields = '__all__'
#
#         widgets = {
#             'apper': forms.TextInput(attrs={'class': 'form-control'}),
#             'printer': forms.Select(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#             'room': forms.Select(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
#
#         }
