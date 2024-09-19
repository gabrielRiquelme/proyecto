from django import forms

class Registro(forms.Form):
    username = forms.CharField(required=True,min_length=5,max_length=40,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre de usuario'
    }))
    correo = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Correo Electronico'
    }))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña'
    }))