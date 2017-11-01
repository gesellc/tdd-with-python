from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

def send_login_email(request):
    email = request.POST['email']
    send_mail(
        'Your login link for Superlists',
        'body',
        'noreply@superlists',
        [email])
    return redirect('/')
