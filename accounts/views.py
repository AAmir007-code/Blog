from django.shortcuts import render
from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.


class SignUp(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

class ListAllUsers(generic.ListView):
    model = User
    template_name = 'accounts/showusers.html'
    context_object_name = 'users'