from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return HttpResponse("fnauidgf")

def register(request):
    if request.method == "POST":
        response = HttpResponse()
        response.write("Thanks, " + request.POST['email'])
        return response
    email = request.POST.get('email')
    subject = "Thank you for register"
    message = "This is us world"
    email_from = settings.EMAIL_CONFIG
    recipient_list = email
    send_mail(subject, message, email_from, recipient_list)

    registerForm = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': registerForm})


