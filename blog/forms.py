from django import forms
from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'gambar']
        
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'}),
        }