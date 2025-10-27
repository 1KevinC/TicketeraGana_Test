from django.urls import path
from .views import (
    login_view, logout_view,
    lista_usuarios, nuevo_usuario, crear_usuario,
    home, cartelera, contrataciones, nosotros, compra,
    show1, show2, show3, show4,
    pagar_view  # nueva vista de pago
)
from django.views.generic import TemplateView

urlpatterns = [
    # ---------------------- PÁGINAS PRINCIPALES ----------------------
    path('', home, name='home'),
    path('home/', home, name='home_alt'),

    path('cartelera/', cartelera, name='cartelera'),
    path('contrataciones/', contrataciones, name='contrataciones'),
    path('nosotros/', nosotros, name='nosotros'),

    # ---------------------- AUTENTICACIÓN ----------------------
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # ---------------------- USUARIOS ----------------------
    path('usuarios/', lista_usuarios, name='usuarios_list'),
    path('nuevo-usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),

    # ---------------------- COMPRAS ----------------------
    path('comprar/', compra, name='compra'),
    path('show1/', show1, name='show1'),
    path('show2/', show2, name='show2'),
    path('show3/', show3, name='show3'),
    path('show4/', show4, name='show4'),

    # ---------------------- MERCADO PAGO ----------------------
    path('pagar/<int:idfuncion>/', pagar_view, name='pagar'),

    # Páginas de resultado del pago
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('failure/', TemplateView.as_view(template_name='failure.html'), name='failure'),
    path('pending/', TemplateView.as_view(template_name='pending.html'), name='pending'),
]
