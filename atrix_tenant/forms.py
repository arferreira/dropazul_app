from django import forms
from django.contrib.auth.models import User


# ===================================================
# Login de Inquilinos
# ===================================================

class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs=({'class': 'validate'})), required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs=({'class': 'validate'})), required=True)
    my_user = None  # Si se logea un usuario correctamente entonces se almacena aquí la sesión.

    def clean_password(self):
        from django.contrib.auth import authenticate
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except:
            user = None
        if user:
            user_auth = authenticate(username=user.username, password=self.cleaned_data['password'])
        else:
            user_auth = None
        if user_auth is not None:
            if user.is_active:
                self.my_user = user_auth
                pass
            else:
                raise forms.ValidationError("Lo lamentamos, el usuario se encuentra deshabilitado")
        else:
            raise forms.ValidationError("Email y/o contraseña incorrecta")