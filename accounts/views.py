from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
# Create your views here.



#class SignupPageView(generic.CreateView):
#    form_class = CustomUserCreationForm
#    success_url = reverse_lazy('login')               ....... no need after allauth ........
#    template_name = 'registration/signup.html'