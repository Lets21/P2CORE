from django.urls import path
from django.contrib import admin
from . import views
from .views import dashboard_doctor, dashboard_paciente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('servicios/', views.servicios_view, name='servicios'),  # Agregar esta línea
    path('contactos/', views.contactos_view, name='contactos'),  # Agregar esta línea
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='home'),
    path('dashboard/doctor/', dashboard_doctor, name='dashboard_doctor'),
    path('dashboard/paciente/', dashboard_paciente, name='dashboard_paciente'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('logout/', views.logout_view, name='logout'),
    path('doctores/', views.doctores_view, name='doctores'),
    path('prescripcion/', views.prescripcion_view, name='prescripcion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)