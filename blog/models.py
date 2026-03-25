from django.db import models
from django.contrib.auth.models import User

class Artikel(models.Model):
    
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)
    gambar = models.ImageField(upload_to='gambar_artikel/', null=True, blank=True)
    def __str__(self):
        return self.judul