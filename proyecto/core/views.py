from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

def index(request):
    return render(request, "core/index.html")

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")