from django import forms
from .models import Artikel, Komentar

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'gambar']
        
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'}),
        }

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['isi']
        widgets = {
            'isi': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tulis komentar Anda...'}),
        }