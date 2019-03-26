# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Change to russian language
        username = self.fields['username'].label = 'Логин'
        password = self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем не найден')
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')



class RegistrationForm(forms.ModelForm):

    password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        )
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # Change to russian language
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['password_check'].label = 'Повторите пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Ваш Email'

        # Change help text
        self.fields['first_name'].help_text = 'Имя'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')

        if password != password_check:
            raise forms.ValidationError('Ваши пароли не совпадают')
