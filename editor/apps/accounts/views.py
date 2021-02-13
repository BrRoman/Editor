""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import EditorLoginForm


class EditorLoginView(LoginView):
    """ Login view. """
    form_class = EditorLoginForm
    template_name = 'accounts/login.html'
