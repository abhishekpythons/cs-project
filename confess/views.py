from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.message import EmailMessage
from . import config

def view_form(request):
    return render(request, 'login.html')

def send_email(From_name, To_email, msg):
        message = EmailMessage()
        message['Subject'] = f'confession from: {From_name}'
        message['From'] = config.EMAIL_ADDRESS
        message['To'] = To_email
        msg = str( msg + '\n'*10 + 'This is a mail send via confessinator.herokuapp.com \n here name(%s) shown may be real or fake.\nBut intentions and emotions are true. \nOur Team is doing work of filling gaps.\nRegards confessinator team :)'%From_name)
        message.set_content(msg)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
            smtp.send_message(message)



@csrf_exempt
def read_form(request):
    From_name = request.POST['From_name']
    To_email = request.POST['To_email']
    msg = request.POST['msg']
    if To_email == '':
        messages = {'type': 'error', 'color': 'red', 'message': 'email whom to be send not provided'}
        return render(request, 'confession.html', messages)
    elif msg == '':
        messages = {'type': 'error', 'color': 'red', 'message': 'message is empty'}
        return render(request, 'confession.html', messages)
    else:
        send_email(From_name, To_email, msg)
        messages = {'type': 'success', 'color': 'purple', 'message': 'confession send successfully'}
        return render(request, 'index.html', messages)
        # else:
        #     messages = {'type': 'error', 'color': 'red', 'message': 'confession not send! Try Again !!'}
        #     return render(request, 'confession.html', messages)