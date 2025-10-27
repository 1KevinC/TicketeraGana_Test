from django import forms
from .models_usuarios import Usuario

class UsuarioPerfilForm(forms.ModelForm):
    # contraseña editable, pero NO se muestra el valor actual
    contrasena = forms.CharField(
        label="Contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Dejar vacío para no cambiar"})
    )

    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "email", "contrasena"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "input"}),
            "apellido": forms.TextInput(attrs={"class": "input"}),
            "email": forms.EmailInput(attrs={"class": "input"}),
        }

    def __init__(self, *args, **kwargs):
        # aseguramos que el password no venga precargado
        super().__init__(*args, **kwargs)
        self.fields["contrasena"].initial = ""

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        # respetá la unicidad, excluyendo el propio registro
        qs = Usuario.objects.filter(email__iexact=email)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ese email ya está en uso.")
        return email

    def clean_contrasena(self):
        pwd = self.cleaned_data.get("contrasena", "")
        # si lo deja vacío, mantenemos la contraseña anterior
        if not pwd and self.instance and self.instance.pk:
            return self.instance.contrasena
        if pwd and len(pwd) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return pwd
