from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models_usuarios import Usuario

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("AUTH start:", username)
        if not username or not password:
            print("AUTH missing data")
            return None
        try:
            u = Usuario.objects.get(email=username)
            print("AUTH got user from DB")
        except Usuario.DoesNotExist:
            print("AUTH user not found")
            return None

        if u.contrasena == password:
            user, _ = User.objects.get_or_create(
                username=u.email,
                defaults={
                    'email': u.email or '',
                    'first_name': u.nombre or '',
                    'last_name': u.apellido or '',
                }
            )
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
            print("AUTH success -> returning user")
            return user
        print("AUTH wrong password")
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
