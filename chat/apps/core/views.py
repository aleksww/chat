import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from .models import Message, Chat
from core.forms import LoginForm

log = logging.getLogger(__name__)


@login_required
def chat(request):
    users = Chat.objects.get(name='chat').user
    messages = reversed(Message.objects.order_by('-timestamp')[:10])
    return render(request, "chat.html", {'messages': messages, 'users': users})


def logout_view(request):
    user = request.user
    logout(request)

    chat = Chat.objects.get(name='chat')
    chat.user.remove(user)
    log.info('User %s log out', user)

    return redirect(settings.LOGIN_URL)


def login_view(request):
    form = LoginForm(request.POST or None)
    context = { 'form': form, }
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            chat, created = Chat.objects.get_or_create(name='chat')
            chat.user.add(user)
            log.info('User %s log in', user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'registration/login.html', context)