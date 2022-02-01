from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from acc.forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
class SingUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index', current_app='summarizer')
    template_name = 'registration/signup.html'

    # Per login automatikisht pas regjistrimit
    def form_valid(self, form):
        response = super().form_valid(form)
        # merr username dhe password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # ben authenticate user pastaj login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
