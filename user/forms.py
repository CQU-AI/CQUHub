from django import forms

from captcha.fields import CaptchaField

class Login(forms.Form):
    username = forms.CharField(label='学号', required=True, max_length=150, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "id_login", "placeholder": "请输入学号"}))
    password = forms.CharField(label='密码', required=True, min_length=5, widget=forms.PasswordInput(
        attrs={"class": "form-control", "id": "id_password", "name": "password", "placeholder": "请输入密码"}))


class Register(forms.Form):
    username = forms.CharField(required=True, max_length=150, min_length=2, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "id_username", "type": "text", "placeholder": "请输入您的学号"}))
    password = forms.CharField(required=True, max_length=20, min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control", "id": "id_password1", "placeholder": "请输入您的密码"}))
    passwordConfirm = forms.CharField(required=True, max_length=20, min_length=6,
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "id": "id_password1", "placeholder": "请再次输入您的密码"}))
    captcha = CaptchaField(error_messages={'message': '验证码输入错误'})
