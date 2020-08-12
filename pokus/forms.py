from django import forms
from .models import Komentar

class ZboziKoment(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ["hlavicka","koment"]