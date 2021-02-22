from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

def view_form(request):
    return render(request, 'registration_page.html')

def save(username,password,email,ph_no):
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cur = conn.cursor()
    cur.execute(f'insert into user_details(username, password, email, ph_no) values("{username}","{password}","{email}","{ph_no}")')
    conn.commit()


@csrf_exempt
def read_form(request):
    username = request.POST['username']
    pwd = request.POST['password']
    email = request.POST['email']
    ph_no = request.POST['ph_no']
    if username == '':
        return HttpResponse('username is empty')
    elif email == '':
        return HttpResponse('email is empty')
    else:
        save(username, pwd, email, ph_no)
        messages.success(request, 'successfully registered !')
        return render(request, 'index.html')