from django.urls import path
from django.views.generic import TemplateView
from . import views  # <- sólo el módulo, nada de "from .views import ..."

urlpatterns = [
    # PÁGINAS PRINCIPALES
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alt'),
    path('cartelera/', views.cartelera, name='cartelera'),
    path('contrataciones/', views.contrataciones, name='contrataciones'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('mi-perfil/', views.mi_perfil_usuario, name='mi_perfil_usuario'),

    # AUTENTICACIÓN
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # USUARIOS
    path('usuarios/', views.lista_usuarios, name='usuarios_list'),
    path('nuevo-usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),

    # COMPRAS / SHOWS
    path('comprar/', views.compra, name='compra'),
    path('show1/', views.show1, name='show1'),
    path('show2/', views.show2, name='show2'),
    path('show3/', views.show3, name='show3'),
    path('show4/', views.show4, name='show4'),

    # MERCADO PAGO
    path("pagar/<int:idfuncion>/", views.pagar_view, name="pagar"),

    # RESULTADOS
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('failure/', TemplateView.as_view(template_name='failure.html'), name='failure'),
    path('pending/', TemplateView.as_view(template_name='pending.html'), name='pending'),
]
