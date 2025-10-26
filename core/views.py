from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.cache import never_cache

from .models_usuarios import Usuario
from .models import Funcion  # usamos la tabla 'funcion' real de Render


# ---------------------- LOGIN / LOGOUT ----------------------

@never_cache
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        username = (request.POST.get('username') or '').strip()
        password = (request.POST.get('password') or '').strip()
        user = authenticate(request, username=username, password=password)

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
            return redirect("home")

        messages.error(request, "Email o contraseña inválidos.")
    return render(request, "login.html", {"form": form})


@never_cache
def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada.")
    return redirect("login")


# ---------------------- USUARIOS ----------------------

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
            messages.error(request, "Email y contraseña son obligatorios.")
            return redirect("nuevo_usuario")

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "El email ya existe en la base.")
            return redirect("nuevo_usuario")

        u = Usuario(
            email=email,
            nombre=nombre,
            apellido=apellido,
            contrasena=password,
            rol='cliente',
            fechaalta=timezone.now(),
        )
        u.save()

        User.objects.get_or_create(
            username=email,
            defaults={'email': email, 'first_name': nombre, 'last_name': apellido}
        )

        messages.success(request, "Cuenta creada. Ahora podés iniciar sesión.")
        return redirect("login")

    return redirect("nuevo_usuario")


# ---------------------- PÁGINAS ESTÁTICAS ----------------------

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


# ---------------------- SHOWS ----------------------

# SHOW 1 - conecta con la tabla "funcion" en Render
def show1(request):
    # Cambiá el idobra según el ID real de "Stand Up de Parejas"
    funciones = Funcion.objects.filter(idobra=12).order_by('fecha', 'hora')

    if request.method == "POST":
        idfuncion = request.POST.get("funcion")
        cantidad = int(request.POST.get("entradas", 1))
        funcion = get_object_or_404(Funcion, pk=idfuncion)

        if cantidad <= funcion.cupo:
            funcion.cupo -= cantidad
            funcion.save(update_fields=["cupo"])
            messages.success(request, f"Compra realizada correctamente. Entradas restantes: {funcion.cupo}")
        else:
            messages.error(request, "No hay suficientes entradas disponibles.")

        return redirect("show1")

    return render(request, 'show1.html', {"funciones": funciones})


def show2(request):
    # Cambiar idobra por el ID de la obra correspondiente
    funciones = Funcion.objects.filter(idobra=9).order_by('fecha', 'hora')

    if request.method == "POST":
        idfuncion = request.POST.get("funcion")
        cantidad = int(request.POST.get("entradas", 1))
        funcion = get_object_or_404(Funcion, pk=idfuncion)

        if cantidad <= funcion.cupo:
            funcion.cupo -= cantidad
            funcion.save(update_fields=["cupo"])
            messages.success(request, f"Compra realizada. Entradas restantes: {funcion.cupo}")
        else:
            messages.error(request, "No hay suficientes entradas disponibles.")

        return redirect("show2")

    return render(request, 'show2.html', {"funciones": funciones})


def show3(request):
    funciones = Funcion.objects.filter(idobra=11).order_by('fecha', 'hora')

    if request.method == "POST":
        idfuncion = request.POST.get("funcion")
        cantidad = int(request.POST.get("entradas", 1))
        funcion = get_object_or_404(Funcion, pk=idfuncion)

        if cantidad <= funcion.cupo:
            funcion.cupo -= cantidad
            funcion.save(update_fields=["cupo"])
            messages.success(request, f"Compra realizada. Entradas restantes: {funcion.cupo}")
        else:
            messages.error(request, "No hay suficientes entradas disponibles.")

        return redirect("show3")

    return render(request, 'show3.html', {"funciones": funciones})


def show4(request):
    funciones = Funcion.objects.filter(idobra=10).order_by('fecha', 'hora')

    if request.method == "POST":
        idfuncion = request.POST.get("funcion")
        cantidad = int(request.POST.get("entradas", 1))
        funcion = get_object_or_404(Funcion, pk=idfuncion)

        if cantidad <= funcion.cupo:
            funcion.cupo -= cantidad
            funcion.save(update_fields=["cupo"])
            messages.success(request, f"Compra realizada. Entradas restantes: {funcion.cupo}")
        else:
            messages.error(request, "No hay suficientes entradas disponibles.")

        return redirect("show4")

    return render(request, 'show4.html', {"funciones": funciones})
