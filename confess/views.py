from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import smtplib
import config

def view_form(request):
    return render(request, 'login.html')

def send_email(From_name, To_email, msg):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = f'From: {From_name} \n {msg}'
            server.sendmail(config.EMAIL_ADDRESS, To_email, message)
            server.quit()
            return True
        except:
            return False

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
        send = send_email(From_name, To_email, msg)
        if send:
            messages = {'type': 'success', 'color': 'purple', 'message': 'confession send successfully'}
            return render(request, 'index.html', messages)
        else:
            messages = {'type': 'error', 'color': 'red', 'message': 'confession not send! Try Again !!'}
            return render(request, 'confession.html', messages)