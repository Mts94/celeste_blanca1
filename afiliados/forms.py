from django import forms
from .models import Afiliado


class AfiliadoForm(forms.ModelForm):
    class Meta:
        model = Afiliado
        fields = '__all__'
        widgets = {
            'apellido_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Selecciona un archivo Excel")



class Meta:
    model = Afiliado
    fields = "__all__"
    widgets = {
            "apellido_nombre": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "localidad": forms.TextInput(attrs={"class": "form-control"}),
            "horario": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "observacion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

