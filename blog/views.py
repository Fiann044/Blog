from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artikel
from .forms import ArtikelForm
from django.contrib.auth.forms import UserCreationForm 
from .models import Artikel, Komentar
from .forms import ArtikelForm, KomentarForm


def halaman_utama(request):
    artikel_dari_db = Artikel.objects.all()
    data_konteks = {
        'nama': 'Fian Gawul',
        'status': 'Mahasiswa',
        'daftar_artikel': artikel_dari_db, 
    }
    return render(request, 'blog/index.html', data_konteks)


def detail_artikel(request, id):
    artikel_pilihan = get_object_or_404(Artikel, id=id)
    

    daftar_komentar = artikel_pilihan.komentar.all().order_by('-tanggal_dibuat')
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form_komentar = KomentarForm(request.POST)
            if form_komentar.is_valid():
                komentar_baru = form_komentar.save(commit=False)
                komentar_baru.artikel = artikel_pilihan
                komentar_baru.penulis = request.user
                komentar_baru.save()
                return redirect('detail_artikel', id=artikel_pilihan.id)
        else:
            return redirect('login')
    else:
        form_komentar = KomentarForm()

    
    return render(request, 'blog/detail.html', {
        'artikel': artikel_pilihan,
        'daftar_komentar': daftar_komentar,
        'form_komentar': form_komentar
    })


@login_required(login_url='login')
def tambah_artikel(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST, request.FILES)
        if form.is_valid():
            artikel_baru = form.save(commit=False) 
            artikel_baru.penulis = request.user    
            artikel_baru.save()                    
            return redirect('halaman_utama') 
    else:
        form = ArtikelForm()

    return render(request, 'blog/tambah.html', {'form': form})
    

@login_required(login_url='login')
def hapus_artikel(request, id):
    artikel_pilihan = get_object_or_404(Artikel, id=id)
    
  
    if request.user == artikel_pilihan.penulis:
        if request.method == 'POST':
            artikel_pilihan.delete()          
            return redirect('halaman_utama')  
        return render(request, 'blog/hapus.html', {'artikel': artikel_pilihan})
    else:

        return redirect('halaman_utama')


@login_required(login_url='login')
def artikel_saya(request):
 
    artikel_pribadi = Artikel.objects.filter(penulis=request.user)
    return render(request, 'blog/artikel_saya.html', {'daftar_artikel': artikel_pribadi})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form': form})

@login_required(login_url='login')
def edit_artikel(request, id):
   
    artikel_pilihan = get_object_or_404(Artikel, id=id)
    
   
    if request.user != artikel_pilihan.penulis:
        return redirect('halaman_utama')
        
    if request.method == 'POST':
   
        form = ArtikelForm(request.POST, request.FILES, instance=artikel_pilihan)
        
        if form.is_valid():
            form.save()
          
            return redirect('detail_artikel', id=artikel_pilihan.id)
    else:
       
        form = ArtikelForm(instance=artikel_pilihan)

    return render(request, 'blog/edit.html', {'form': form, 'artikel': artikel_pilihan})

