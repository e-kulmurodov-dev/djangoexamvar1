# ----------------------------------- Email verification 👇------------------------------------------------------
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import ListView, DetailView

from .forms import CustomUserCreationForm
from .models import CustomUser
from .tasks import send_activation_email
from .tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            send_activation_email.delay(user.id, current_site.domain)

            return redirect('account_activation_sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and not user.activation_link_used and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.activation_link_used = True
        user.save()
        login(request, user)
        return redirect('account_activation_complete')
    else:
        return HttpResponseBadRequest('Activation link is invalid or has already been used!')


def account_activation_complete(request):
    return render(request, 'account_activation_complete.html')


class UserProfile(DetailView):
    queryset = CustomUser.objects.all()
    template_name = 'user_profile.html'
    context_object_name = 'user'


class UserListView(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'blog-details-left-sidebar.html'
    context_object_name = 'blogs'
