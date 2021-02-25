from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector, csv, time, os
from django.conf import settings

create_table={'registration':'''create table registration(
                                                registration_id int(7) primary key auto_increment,
                                                user_name char(20),
                                                password char(20),
                                                email_id varchar(40))''',
                          'application':'''create table application(
                                                application_no int(7) primary key auto_increment,
                                                registration_id int(7),
                                                title varchar(200) not null ,
                                                lab char(10) ,
                                                technology_cluster char(50),
                                                filing_year int(4),
                                                team_allot char(10) not null,
                                                status char(20) default "not checked")''',
                'checking_teams':'''create table checking_teams(
                                                team_id char(7) primary key,
                                                no_of_members int(2),
                                                authentication_pin char(16) not null,
                                                on_mission bool not null default false)''',
            'patents_confirmed':'''create table patents_confirmed(
                                               patent_id int(7) primary key,
                                               application_no int(7) ,
                                               checked_by char(20),
                                               filing_year int(4) not null)'''
                        }


def view_form(request):
    connect_to_server()
    return render(request, 'registration_page.html')


def loading_animation(type, msg, sec=1):
    print(f'[{type}] \t {msg}')
    time.sleep(sec)
    pass
    #create message here


def connect_to_server():
    loading_animation('action', 'connecting to server', 1)
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk', database='sql12394795')
    if conn.is_connected():
        loading_animation('info', 'connected')
    cur = conn.cursor()
    cur.execute('show tables;')
    tables_in_db = [i[0] for i in cur]
    for table in create_table:
        if table not in tables_in_db:
            loading_animation('action', f'creating table {table}', 3)
            cur.execute(create_table[table])
        else:
            loading_animation('info', f'table {table} found in database')
    cur.execute('select count(*) from checking_teams')
    no_of_teams = cur.fetchall()[0][0]

    if no_of_teams == 0:
        file_path = os.path.join(settings.MEDIA_URL, 'confidential.csv')
        file = open(file_path, 'r')
        reader = csv.reader(file)
        for row in reader:
            print(row)
            # row[1] = int(row[1])
            # row = tuple(row)
            # cur.execute(f'insert into checking_teams(team_id,no_of_members,authentication_pin) values{row}')
            # conn.commit()
        loading_animation('info', 'table checking teams filled')
        file.close()


@csrf_exempt
def read_form(request):
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk',
                                   database='sql12394795')
    if conn.is_connected():
        loading_animation('info', 'connected')
    cur = conn.cursor()
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    if conn.is_connected():
        loading_animation('info','connected')
    cur.execute(f'insert into registration(user_name,password,email_id) values("{username}","{password}","{email}")')
    loading_animation('info',"registered")
    conn.commit()
    cur.execute('select * from registration')
    rid = cur.fetchall()[-1][0]
    loading_animation('info', 'your registeration id is %d'%rid)

    while len(password)<8:
        return render(request, 'registration.html', {'type': 'error', 'message': 'password is too short'})
    while len(password)>20:
        return render(request, 'registration.html', {'type': 'error', 'message': 'password is too long'})
    if username == '':
        messages = {'type': 'error', 'color': 'red', 'message': 'username is empty'}
        return render(request, 'registration_page.html', messages)
    elif email == '':
        messages = {'type': 'error', 'color': 'red', 'message': 'email is empty'}
        return render(request, 'registration_page.html', messages)
    elif pwd != confirm_pwd:
        messages = {'type': 'error', 'color': 'red', 'message': 'confirm email not matched'}
        return render(request, 'registration_page.html', messages)
    elif email in get_emails():
        messages = {'type': 'error', 'color': 'red', 'message': 'email already exists', 'page': 'registration'}
        return render(request, 'registration_page.html', messages)
    else:
        save(username, pwd, email, ph_no)
        messages = {'type': 'success', 'color': 'purple', 'message': 'registered successfully',}
        return render(request, 'login_page.html', messages)