# coding=utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'username',
                   'autofocus': ''}))
    password = forms.CharField(
        label=_("Password"),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'password',
                   'type': 'password'}))
