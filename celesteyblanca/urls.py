from django.contrib import admin
from django.urls import path, include
from afiliados import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Raíz redirige al login
    path("", lambda request: redirect("login")),
    
    # Login / Logout
    path('afiliados/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Admin y CRUD
    path("admin/", admin.site.urls),
    path("afiliados/", include("afiliados.urls")),
    
    # Excel (global)
    path("carga_excel/", views.upload_excel, name="carga_excel"),
    path("exportar_excel/", views.exportar_excel, name="exportar_excel"),
]