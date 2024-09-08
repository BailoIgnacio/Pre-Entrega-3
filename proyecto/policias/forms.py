from django import forms
from .models import Policia
from django.core.exceptions import ValidationError
class PoliciaForm(forms.ModelForm):
    class Meta:
        model = Policia
        fields = "__all__"

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre", "")
        if not nombre.isalpha():
            raise ValidationError("Solo se pueden introducir letras")
        
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidationError("El nombre ingresado no puede tener menos de 3 letras y mas de 50")
        
        return nombre