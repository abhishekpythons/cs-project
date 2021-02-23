from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

def view_form(request):
    return render(request, 'registration_page.html')

def save(username,password,email,ph_no):
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk', database='sql12394795')
    cur = conn.cursor()
    cur.execute(f'insert into user_details(username, password, email, ph_no) values("{username}","{password}","{email}","{ph_no}")')
    conn.commit()

def get_emails():
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk', database='sql12394795')
    cur = conn.cursor()
    cur.execute(f'select email from user_details')
    data = cur.fetchall()
    print(data)
    data = [i[0] for i in data]
    return data


@csrf_exempt
def read_form(request):
    username = request.POST['username']
    pwd = request.POST['password']
    email = request.POST['email']
    ph_no = request.POST['ph_no']
    if username == '':
        return HttpResponse('<h1 style="color:red"> username is empty </h1>')
    elif email == '':
        return HttpResponse('<h1 style="color:red"> email is empty </h1>')
    else:
        if email not in get_emails():
            save(username, pwd, email, ph_no)
            messages = {'type': 'success', 'color': 'purple', 'message': 'registered successfully',}
            return render(request, 'login_page.html', messages)
        else:
            messages = {'type': 'error', 'color': 'red', 'message': 'email already exists', 'page': 'registration'}
            return render(request, 'registration_page.html', messages)