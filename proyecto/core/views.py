from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserProfileForm
def index(request):
    return render(request, "core/index.html")

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "core/profile.html"
    success_url = reverse_lazy("core:login")

    def get_object(self):
        return self.request.user