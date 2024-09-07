from django import forms
from django.core.exceptions import ValidationError
from .models import Prision, Presos

class PrisionForm(forms.ModelForm):
    class Meta:
        model = Prision
        fields = "__all__"

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre", "")
        if not nombre.isalpha():
            raise ValidationError("El nombre solo puede tener letras")
        
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidationError("El nombre debe tener un largo minimo de 3 letras y uno maximo de 50")
        
        return nombre
    
class PresosForm(forms.ModelForm):
    class Meta:
        model = Presos
        fields = "__all__"