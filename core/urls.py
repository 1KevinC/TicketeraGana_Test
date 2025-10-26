from django.urls import path
from .views import (
    login_view, logout_view,
    lista_usuarios, nuevo_usuario, crear_usuario,
    home, cartelera, contrataciones, nosotros, compra,
    show1, show2, show3, show4
)

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home_alt'),

    path('cartelera/', cartelera, name='cartelera'),
    path('contrataciones/', contrataciones, name='contrataciones'),
    path('nosotros/', nosotros, name='nosotros'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('usuarios/', lista_usuarios, name='usuarios_list'),
    path('nuevo-usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),

    path('comprar/', compra, name='compra'),
    path('show1/', show1, name='show1'),
    path('show2/', show2, name='show2'),
    path('show3/', show3, name='show3'),
    path('show4/', show4, name='show4'),
]
