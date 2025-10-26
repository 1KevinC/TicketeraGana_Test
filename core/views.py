# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.cache import never_cache

from .models_usuarios import Usuario
# core/views.py (arriba, junto con otros imports)
from django.views.decorators.cache import never_cache


@never_cache
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        username = (request.POST.get('username') or '').strip()
        password = (request.POST.get('password') or '').strip()
        print("LOGIN POST:", username)

        user = authenticate(request, username=username, password=password)
        print("LOGIN authenticate returned:", bool(user))

        if user is not None:
            try:
                u = Usuario.objects.get(email=username)
                changed = False
                if user.first_name != (u.nombre or ''):
                    user.first_name = u.nombre or ''
                    changed = True
                if user.last_name != (u.apellido or ''):
                    user.last_name = u.apellido or ''
                    changed = True
                if user.email != (u.email or ''):
                    user.email = u.email or ''
                    changed = True
                if changed:
                    user.save()
            except Usuario.DoesNotExist:
                pass

            login(request, user)
            next_url = request.POST.get("next")
            return redirect(next_url or "home")

        messages.error(request, "Email o contrasena invalidos.")

    return render(request, "login.html", {"form": form})


@never_cache
def logout_view(request):
    logout(request)
    messages.info(request, "Sesion cerrada.")
    return redirect("login")


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios_list.html', {'usuarios': usuarios})


def nuevo_usuario(request):
    return render(request, 'nuevo_usuario.html')


def crear_usuario(request):
    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        apellido = (request.POST.get("apellido") or "").strip()
        email = (request.POST.get("email") or "").strip()
        password = (request.POST.get("password") or "").strip()

        if not (email and password):
            messages.error(request, "Email y contrasena son obligatorios.")
            return redirect("nuevo_usuario")

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "El email ya existe en la base.")
            return redirect("nuevo_usuario")

        # save in your table `usuario`
        u = Usuario(
            email=email,
            nombre=nombre,
            apellido=apellido,
            contrasena=password,  # WARNING: plain text
            rol='cliente',
            fechaalta=timezone.now(),
        )
        u.save()

        # ensure shadow user exists for sessions
        User.objects.get_or_create(
            username=email,
            defaults={'email': email, 'first_name': nombre, 'last_name': apellido}
        )

        messages.success(request, "Cuenta creada. Ahora podes iniciar sesion.")
        return redirect("login")

    return redirect("nuevo_usuario")


@never_cache
def home(request):
    return render(request, 'home.html')



def cartelera(request):
    return render(request, 'cartelera.html')


def contrataciones(request):
    return render(request, 'contrataciones.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def compra(request):
    return render(request, 'compra.html')


def show1(request):
    return render(request, 'show1.html')


def show2(request):
    return render(request, 'show2.html')


def show3(request):
    return render(request, 'show3.html')


def show4(request):
    return render(request, 'show4.html')
