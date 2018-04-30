# -*- coding: utf-8 -*-
"""Views for webfront App."""

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
import requests
import json
from webfront.forms import SignUpForm
from django.conf import settings

URLS = settings.URLS


class ResetPasswordView(PasswordResetView):
    """View for resetting password.

    Attributes:
        email_template_name (str): Description
        success_url (TYPE): Description
        template_name (str): Description
    """

    email_template_name = 'reset_password_email.html'
    success_url = reverse_lazy('reset_password_done')
    template_name = 'reset_password.html'


# pylint: disable=too-many-ancestors
class ResetPasswordDoneView(PasswordResetDoneView):
    """View after user chooses to reset his password.

    Attributes:
        template_name (str): Description
    """

    template_name = 'reset_password_done.html'


# pylint: disable=too-many-ancestors
class ResetPasswordConfirmView(PasswordResetConfirmView):
    """View for confirming to reset password.

    Attributes:
        success_url (TYPE): Description
        template_name (str): Description
    """

    template_name = 'reset_password_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    """View to indicate resetting password completed.

    Attributes:
        template_name (str): Description
    """

    template_name = 'reset_password_complete.html'


class LoginView(TemplateView):
    """View for user login.

    Attributes:
        template_name (str): Description
    """

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        """Handle user login request.

        Args:
            request (TYPE): Description

        Returns:
            TYPE: rendered html page
        """
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth = requests.post(URLS['auth'] + 'get_jwt/', data={
                'username': username,
                'password': password
            })
            if auth.status_code == 200:
                result = json.loads(auth.text)
                jwt = result['token']
                sub_path = request.GET.get('next')
                if sub_path:
                    response = redirect(URLS['base'] + sub_path.lstrip('/'))
                else:
                    response = redirect(URLS['main'])
                response.set_cookie('JWT', jwt)
                return response

        args = {'form': form}
        return render(request, self.template_name, args)


class SignUpView(TemplateView):
    """View for user sign up.

    Attributes:
        template_name (str): Description
    """

    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        """Handle user sign up request.

        Args:
            request (TYPE): Description

        Returns:
            TYPE: rendered html page
        """
        form = SignUpForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                new_user = form.save()
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
                login(request, new_user)
                return redirect('home')
        args = {'form': form}
        return render(request, self.template_name, args)


class HomeView(TemplateView):
    """View for temperoray Home.
    Will be removed after the Main app is implemented.

    Attributes:
        template_name (str): Description
    """

    template_name = 'home.html'

    def post(self, request):
        """Logout user.

        Args:
            request (TYPE): Description

        Returns:
            TYPE: Description
        """
        logout(request)
        return redirect('login')
