from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Message


@login_required
def chat(request):
    messages = Message.objects.order_by('-timestamp')[:10]
    return render(request, "chat.html", {'messages': messages})