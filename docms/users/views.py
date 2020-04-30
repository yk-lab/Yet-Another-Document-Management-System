from django.contrib.auth.views import (
    LoginView
)
from .forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'
