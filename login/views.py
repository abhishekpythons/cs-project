from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mysql.connector


def login_form(request):
    return render(request, 'login_page.html')


def fetch_user_and_pass(email):
    credentials = {}
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk',
                                   database='sql12394795')
    cur = conn.cursor()
    cur.execute('select email from user_details')
    data = cur.fetchall()
    data = [i[0] for i in data]
    if email in data:
        cur.execute(f'select username, password from user_details where email="{email}"')
        data = cur.fetchall()
        credentials['email'] = email
        print(data)
        credentials['username'] = data[0][0]
        credentials['password'] = data[0][1]
        print(credentials)
        return credentials
    else:
        return None


@csrf_exempt
def view_form(request):
    email = request.POST['email']
    password = request.POST['password']
    credentials = fetch_user_and_pass(email)
    if credentials:
        if password == credentials['password']:
            # return HttpResponse(f"<h1 style='color:red'> Welcome, {username} ! </h1>")
            return render(request, 'confession.html', credentials)
        else:
            return render(request, 'login_page.html',
                          {'type': 'error', 'color': 'red', 'message': 'password is incorrect'})
    else:
        # return HttpResponse(f' sorry username or password is incorrect')
        return render(request, 'login_page.html', {'type': 'error', 'color': 'red', 'message': 'username is incorrect'})
# Create your views here.
