from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

# Create your views here.


@csrf_exempt
def send_email(request):
    # send email
    # redirect back to portfolio
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        subject = request.POST['name']
        sender = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']

        email = sender + '\n' + subject + '\n' + phone + '\n' + message

        recipients = ['awelch@basecampcodingacademy.org']

        send_mail(
            subject, email,
            'postmaster@sandbox8d3f7045f73e4171b813bb268ab8c95a.mailgun.org',
            recipients)
        return HttpResponseRedirect('/static/thanks.html')

    return HttpResponseRedirect('/static/contact.html')
