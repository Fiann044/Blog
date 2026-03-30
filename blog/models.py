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
        #fitur komentar
class Komentar(models.Model):
    artikel = models.ForeignKey(Artikel, related_name='komentar', on_delete=models.CASCADE)
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    isi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Komentar oleh {self.penulis.username} di {self.artikel.judul}"
