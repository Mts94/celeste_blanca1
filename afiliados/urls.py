from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_afiliados, name='lista_afiliados'),
    path('crear/', views.crear_afiliado, name='crear_afiliado'),
    path('editar/<int:pk>/', views.editar_afiliado, name='editar_afiliado'),
    path('eliminar/<int:pk>/', views.eliminar_afiliado, name='eliminar_afiliado'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('login/', auth_views.LoginView.as_view(template_name='afiliados/login.html'), name='login'),
    
    
]
