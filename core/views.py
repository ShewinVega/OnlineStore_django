from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from OnlineStore import settings
from .forms import ContactForm
# Create your views here.

def home(request):
    return render(request,'core/formulario_contacto.html')


def contact(request):
    if request.method == 'POST':

        myform = ContactForm(request.POST) 

        if myform.is_valid():

            data = myform.cleaned_data
            send_mail(
                data['subject'],
                data['message'],
                data.get('email',''),
                [settings.EMAIL_DESTINATARIO],
            )

            return render(request,'core/thanks.html')
    else:
        myform = ContactForm()
    
    return render(request, 'core/formulario_contacto.html',{'form':myform} )









# def contact(request):
#    if request.method=='POST':
#       subject = request.POST['subject']
#       message = request.POST['message']
#       email_from = settings.EMAIL_HOST_USER
#        recipient_list = ['edwinvega.aid@gmail.com']
#
#        if subject and message and email_from:
#            send_mail(subject,message,email_from,recipient_list)
#            return render(request,'core/thanks.html')
#        else:
#            return HttpResponse('Ingrese todos los campos requeridos')
#
#    return render(request,'core/contacts.html')