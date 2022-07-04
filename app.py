from flask import Flask, redirect, url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/')
def homepage():
    return render_template('homePageNew.html')


@app.route('/contact')
def contact_page():
    return render_template('contactNew.html')


@app.route('/assignment3_1')
def assignment3_1_page():
    user = {'first_name': 'OFir', 'last_name': 'azULay', 'ID': '319145959', 'email': 'ofirazu@post.bgu.ac.il','marital_status': 'Single'}
    #user = ''
    hobbies = ['Dance', 'fashiON design', 'Cooking', 'cooking', 'Watching movies', 'prograMMing']
    #hobbies = ''
    preferences_in_music_dict = {'Latin': ['Enrique Iglesias', 'NICKY JAM', 'Manuel Turizo'],
                                'poP': ['Calvin Harris', 'Rihanna', 'dua lipa'],
                                'techno': ['Millero', 'Adriatique', 'artbat','polo&pan', 'ARtbat'],
                                'Israeli': ['Ishay Ribo', 'Natan Goshen', 'Odaya','Noa Kirel', 'Odaya', 'Odaya', 'OdaYa'],
                                 '':['Sean Paul','Eminem']}
    #the values above includs duplicates in order to demonstrate the effectiveness of the filters

    favorit_singer = 'Rihanna'
    session['favorit_singer'] = favorit_singer
    return render_template('assignment3_1.html',
                           user=user,
                           hobbies=hobbies,
                           preferences_in_music_dict=preferences_in_music_dict,
                           favorit_singer=favorit_singer)

users_list = {
        'user1': {'user_name': 'Ofir', 'user_nickName': 'ofirA', 'user_email': 'ofirazu@post.bgu.ac.il', 'user_Gender': 'female', 'user_age': '25','user_ID': '319145959', 'user_password': 'oA319145959'},
        'user2': {'user_name': 'Gal', 'user_nickName': 'galgal', 'user_email': 'galohayon@gmail.com', 'user_Gender': 'female', 'user_age': '27','user_ID': '317485930', 'user_password': 'ggg999Oh123'},
        'user3': {'user_name': 'May', 'user_nickName': 'maya', 'user_email': 'mayNeg@post.bgu.ac.il', 'user_Gender': 'male', 'user_age': '22','user_ID': '395837509', 'user_password': 'mayaMaya123'},
        'user4': {'user_name': 'Ron', 'user_nickName': 'ronkishot', 'user_email': 'ron26@post.bgu.ac.il', 'user_Gender': 'female', 'user_age': '31','user_ID': '219567839', 'user_password': 'Ron987654S'},
        'user5': {'user_name': 'Shir', 'user_nickName': 'shirki', 'user_email': 'shir1996@gmail.com', 'user_Gender': 'male', 'user_age': '29','user_ID': '201085670', 'user_password': 'ShShSh666'},
        'user6': {'user_name': 'Noa', 'user_nickName': 'nushiZak', 'user_email': 'noaZlo30@gmail.com', 'user_Gender': 'female', 'user_age': '26','user_ID': '204627305', 'user_password': 'Noa5060Zak'}
    }


# one time use function in order to add users list from assignment3

# @app.route('/insert_user')
# def insert_userList():
#     for u_id, u_info in users_list.items():
#         user_name = u_info['user_name']
#         user_nickName = u_info['user_nickName']
#         user_email = u_info['user_email']
#         user_Gender = u_info['user_Gender']
#         user_ID = u_info['user_ID']
#         user_age = u_info['user_age']
#         user_password = u_info['user_password']
#         query = "INSERT INTO users(user_name, user_nickName, user_email,user_Gender,user_ID,user_age,user_password) VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s')" % (user_name, user_nickName, user_email,user_Gender,user_ID,user_age,user_password)
#         interact_db(query=query, query_type='commit')
#     return redirect('/assignment3_2')
#


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_page():
    if request.method == 'GET':
        finduser = False
        if  'user_email' in request.args or 'user_ID' in request.args:
                if  request.args['user_email'] =='' and request.args['user_ID'] =='':
                    return render_template('assignment3_2.html',
                                users_list=users_list)
                else:
                    for u_id, u_info in users_list.items():
                            for key in u_info:
                                if  key == 'user_email' or key == 'user_ID':
                                  if (u_info[key] == request.args[key]):
                                    finduser=True
                                    user_name = u_info['user_name']
                                    user_nickName = u_info['user_nickName']
                                    user_email = u_info['user_email']
                                    user_Gender = u_info['user_Gender']
                                    user_age = u_info['user_age']
                                    user_ID = u_info['user_ID']
                                    return render_template('assignment3_2.html',
                                                           user_name=user_name,
                                                           user_nickName=user_nickName,
                                                           user_email=user_email,
                                                           user_Gender=user_Gender,
                                                           user_age=user_age,
                                                           user_ID=user_ID)
                    if finduser == False:
                        return render_template('assignment3_2.html',
                                               message='user not found.')

    elif request.method == 'POST':
            user_name = request.form['user_name']
            user_ID = request.form['user_ID']
            password = request.form['user_password']
            user_nickName = request.form['user_nickName']
            user_Gender = request.form['user_Gender']
            user_email = request.form['user_email']
            user_age = request.form['user_age']

            for u_id, u_info in users_list.items():
                for key in u_info:
                    if key == 'user_ID':
                        if u_info[key] == user_ID:
                            return render_template('assignment3_2.html',
                                                   RegistrationMessage='ID already exists in the system ')
                    if key == 'user_email':
                        if u_info[key] == user_email:
                            return render_template('assignment3_2.html',
                                                   RegistrationMessage='email already exists in the system ')

            session['username'] = user_name
            session['registered'] = True
            newUserInfo = {'user_name': user_name, 'user_nickName': user_nickName, 'user_email': user_email, 'user_Gender': user_Gender, 'user_age': user_age, 'user_ID': user_ID, 'user_password': password}
            users_list['user' + str((len(users_list.keys())+1))] = newUserInfo
            return render_template('assignment3_2.html',
                                             RegistrationMessage='Success',
                                            username=user_name)


    return render_template('assignment3_2.html')


@app.route('/log_out')
def logout_func():
    session['registered'] = False
    session.clear()
    return redirect(url_for('assignment3_2_page'))


@app.route('/mySong')
def FavSinger_func():
    return redirect("https://www.youtube.com/" + session['favorit_singer'])


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='web4_schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value



if __name__ == '__main__':
    app.run(debug=True)

#app.config.from_pyfile('settings.py')

from assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)