from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.halaman_utama, name='halaman_utama'),
    path('artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),
    path('tambah/', views.tambah_artikel, name='tambah_artikel'),
    path('artikel/<int:id>/hapus/', views.hapus_artikel, name='hapus_artikel'),
    
    path('artikel-saya/', views.artikel_saya, name='artikel_saya'),
    
    #  Rute Autentikasi 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # edit artikel
    path('artikel/<int:id>/edit/', views.edit_artikel, name='edit_artikel'),
    path('artikel-saya/', views.artikel_saya, name='artikel_saya'),
]