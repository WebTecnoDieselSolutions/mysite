from http.client import HTTPResponse
from io import StringIO
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "home.html")

def loading(request):

    return render(request, "loading.html")

def servicios(request):

    return render(request,"servicios.html")

def nosotros(request):

    return render(request, "nosotros.html")

def contacto(request):

    if request.method == 'POST':
        if request.method == 'POST':

            subject = request.POST["asunto"] + "    Compañía: " + request.POST["company"]
            message = "Contestar a la dirección: " + request.POST["email"] + "\n" + request.POST["mensaje"]
            email_from = settings.EMAIL_HOST_USER

            #Lista de las pobres almas a las que les llega el spam
            recipient_list = ["tecnodieselmex@gmail.com", "homie211891@gmail.com", "pillitus_@hotmail.com"]
            send_mail(subject, message, email_from, recipient_list)

            return render(request, "thankyou.html")

    return render(request, "contacto.html")