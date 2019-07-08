# -*- coding: utf-8 -*-
from django import forms

from captcha.fields import CaptchaField, CaptchaTextInput


class Login(forms.Form):
    username = forms.CharField(
        label="学号",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "id_login", "placeholder": "请输入学号"}
        ),
    )
    password = forms.CharField(
        label="密码",
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "id_password",
                "name": "password",
                "placeholder": "请输入密码",
            }
        ),
    )


class Register(forms.Form):
    # 学号
    username = forms.CharField(
        required=True,
        max_length=20,
        min_length=8,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "id_username",
                "type": "text",
                "placeholder": "请输入您的学号",
            }
        ),
    )
    # 昵称
    nickname = forms.CharField(
        required=True,
        max_length=10,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "id_nickname",
                "type": "text",
                "placeholder": "请输入您的昵称",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "id_password1",
                "placeholder": "请输入您的密码",
            }
        ),
    )
    passwordConfirm = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "id_password1",
                "placeholder": "请再次输入您的密码",
            }
        ),
    )
    image = forms.ImageField(required=False)
    captcha = CaptchaField()


class Info(forms.Form):
    nickname = forms.CharField(
        required=False,
        max_length=10,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "id_nickname",
                "type": "text",
                "placeholder": "请输入新的昵称",
            }
        ),
    )
    image = forms.ImageField(required=False)


class Verify(forms.Form):
    veriCode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "请输入邮箱验证码",
            }
        )
    )
