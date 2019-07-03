from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views import generic
from .models import Account

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(ListView):
    template_name = 'home.html' # check conditional render

    def get_queryset(self):
        """Return User Visited Restaurant"""
        return Account.objects.order_by('name')[:5]