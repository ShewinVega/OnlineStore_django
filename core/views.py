from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/contacts.html')

def contacto(request):
    if request.method=='POST':
        subject = request.POST['subject']
        message = request.POST['message']
        #email_from = a