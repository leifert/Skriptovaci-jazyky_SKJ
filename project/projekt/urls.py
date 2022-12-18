"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import volejbal.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', volejbal.views.main, name='main'),
    path('klub/<int:klub_id>/',volejbal.views.klub_info, name='klub_info'),
    path('trener/<int:trener_id>/',volejbal.views.trener_info, name='trener_info'),
    path('hraci-v-klubu/<int:klub_id>/',volejbal.views.klub_hraci, name='klub_hraci'),
    path('hraci/', volejbal.views.seznam_hracu, name='seznam_hracu'),
    path('hrac/<int:hrac_id>/',volejbal.views.hrac_info, name='hrac_info'),
    path('zapasy/', volejbal.views.zapasy, name='seznam_zapasu'),
    path('zapas/<int:zapas_id>/',volejbal.views.zapas_info, name='zapas_info'),
    path('kluby/', volejbal.views.kluby, name='seznam_klubu'),
    path('klub-detail/<int:klub_id>/',volejbal.views.klub_info2, name='klub_info2'),
    path('klub/<int:klub_id>/edit/',volejbal.views.klub_edit, name='klub_edit'),
    path('klub/add/',volejbal.views.klub_add, name='klub_add'),
    path('klub-delete/<int:klub_id>/',volejbal.views.klub_delete, name='klub_delete'),
    path('hrac/<int:hrac_id>/edit/',volejbal.views.hrac_edit, name='hrac_edit'),
    path('hrac-delete/<int:hrac_id>/',volejbal.views.hrac_delete, name='hrac_delete'),
    path('hrac/add/',volejbal.views.hrac_add, name='hrac_add'),
    path('zapas/<int:zapas_id>/edit/', volejbal.views.zapas_edit, name='zapas_edit'),
    path('zapas-delete/<int:zapas_id>/', volejbal.views.zapas_delete, name='zapas_delete'),
    path('zapas/add/', volejbal.views.zapas_add, name='zapas_add'),
    path('hala/', volejbal.views.seznam_hal, name='seznam_hal'),
    path('hala/<int:hala_id>/',volejbal.views.hala_info, name='hala_info'),
    path('hala/<int:hala_id>/edit/', volejbal.views.hala_edit, name='hala_edit'),
    path('hala-delete/<int:hala_id>/', volejbal.views.hala_delete, name='hala_delete'),
    path('hala/add/', volejbal.views.hala_add, name='hala_add'),
    path('adresa/', volejbal.views.seznam_adres, name='seznam_adres'),
    path('adresa/<int:adresa_id>/',volejbal.views.adresa_info, name='adresa_info'),
    path('adresa/<int:adresa_id>/edit/', volejbal.views.adresa_edit, name='adresa_edit'),
    path('adresa-delete/<int:adresa_id>/', volejbal.views.adresa_delete, name='adresa_delete'),
    path('adresa/add/', volejbal.views.adresa_add, name='adresa_add'),
    path('trener/', volejbal.views.seznam_treneru, name='seznam_treneru'),
    path('trener-info/<int:trener_id>/',volejbal.views.trener_info2, name='trener_info2'),
    path('trener/<int:trener_id>/edit/', volejbal.views.trener_edit, name='trener_edit'),
    path('trener-delete/<int:trener_id>/', volejbal.views.trener_delete, name='trener_delete'),
    path('trener/add/', volejbal.views.trener_add, name='trener_add'),
]
