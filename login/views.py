from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

def login_form(request):
    return render(request, 'login_page.html')

def fetch_pass(username):
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk', database='sql12394795')
    cur = conn.cursor()
    cur.execute(f'select password from user_details where username="{username}"')
    data = cur.fetchall()
    print(data[0][0])
    return data[0][0]

@csrf_exempt
def view_form(request):
    credentials={}
    username = request.POST['username']
    password = request.POST['password']
    if password == fetch_pass(username):
        credentials['password'] = password
        credentials['username'] = username
        # return HttpResponse(f"<h1 style='color:red'> Welcome, {username} ! </h1>")
        return render(request, 'dashboard.html', credentials)
    else:
        # return HttpResponse(f' sorry username or password is incorrect')
        return render(request, 'invalid_user.html')
# Create your views here.
