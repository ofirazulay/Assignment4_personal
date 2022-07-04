from flask import render_template, Blueprint, request, redirect,jsonify, url_for,session
import requests
from flask import flash
import app

assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         static_url_path='/assignment_4',
                         template_folder='templates')






@assignment_4.route('/assignment_4')
def assignment_4_page():
    query = 'select * from users'
    users_list = app.interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)

# ------------------------------------------------- #

# -------------------- INSERTION FORM --------------------- #
@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    user_name = request.form['user_name']
    user_ID = request.form['user_ID']
    user_password = request.form['user_password']
    user_nickName = request.form['user_nickName']
    user_Gender = request.form['user_Gender']
    user_email = request.form['user_email']
    user_age = request.form['user_age']

    query = "select * FROM users WHERE user_ID='%s';" % user_ID
    users_list = app.interact_db(query, query_type='fetch')

    if len(users_list) != 0:
        flash("User with id: " + user_ID + " already Exist" ,'error')
        return redirect('/assignment_4')

    else:
        query = "INSERT INTO users(user_name, user_nickName, user_email,user_Gender,user_ID,user_age,user_password) VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s')" % (
                                              user_name, user_nickName, user_email, user_Gender, user_ID, user_age, user_password)
        app.interact_db(query=query, query_type='commit')
        flash("User with id: " + user_ID + "  Successfully inserted", 'success')
        return redirect('/assignment_4')
# ------------------------------------------------- #

# # -------------------- UPDATE FORM --------------------- #
# # -------------------- UPDATE FORM --------------------- #
@assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    user_ID = request.form['user_ID']

    if request.form['user_name'] != '':
        nameToUpdate=request.form['user_name']
        query = "UPDATE users SET user_name = '%s' WHERE user_ID = '%s'" % (nameToUpdate , user_ID)
        app.interact_db(query, query_type='commit')

    if request.form['user_nickName'] != '':
        nickNameToUpdate=request.form['user_nickName']
        query = "UPDATE users SET user_nickName = '%s' WHERE user_ID = '%s'" % (nickNameToUpdate , user_ID)
        app.interact_db(query, query_type='commit')


    if request.form['user_email'] != '':
        emailToUpdate = request.form['user_email']
        query = "UPDATE users SET user_email = '%s' WHERE user_ID = '%s'" % (emailToUpdate, user_ID)
        app.interact_db(query, query_type='commit')


    if request.form['user_Gender'] != '':
        GenderToUpdate = request.form['user_Gender']
        query = "UPDATE users SET user_Gender = '%s' WHERE user_ID = '%s'" % (GenderToUpdate, user_ID)
        app.interact_db(query, query_type='commit')


    if request.form['user_age'] != '':
        ageToUpdate = request.form['user_age']
        query = "UPDATE users SET user_age = '%s' WHERE user_ID = '%s'" % (ageToUpdate, user_ID)
        app.interact_db(query, query_type='commit')


    if request.form['user_password'] != '':
        passwordToUpdate = request.form['user_password']
        query = "UPDATE users SET user_password = '%s' WHERE user_ID = '%s'" % (passwordToUpdate, user_ID)
        app.interact_db(query, query_type='commit')
    flash("User with id: " + user_ID + " Successfully updated",'success')
    return redirect('/assignment_4')




# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_ID = request.form['user_ID']

    query = "select * FROM users WHERE user_ID='%s';" % user_ID
    users_list = app.interact_db(query, query_type='fetch')
    if len(users_list) == 0:
        flash(" user with id: " + user_ID + " does not exist",'error')
        return redirect('/assignment_4')
    else:
        query = "DELETE FROM users WHERE user_ID='%s';" % user_ID
        app.interact_db(query, query_type='commit')
        flash("User with id: " + user_ID +" Successfully deleted",'success')
        return redirect('/assignment_4')


# ------------------------------------------------- #
# ------------------------------------------------- #


@assignment_4.route('/assignment4/users')
def jsonUserTable_func():
    query = 'select * from users'
    users_list = app.interact_db(query, query_type='fetch')
    return jsonify(users_list)


@assignment_4.route('/assignment4/outer_sourse')
def outer_sourse_func():
    return render_template('assignment4_outer_source.html')


@assignment_4.route('/fetch_backEnd')
def fetch_be_func():
    inputID = request.args['user_ID_BE']
    userRes= requests.get(f'https://reqres.in/api/users/{inputID}')
    userData=userRes.json()
    for userData_Key, userData_Values in userData.items():
        for key in userData_Values:
            if key == 'avatar':
                picture = userData_Values['avatar']
            if key == 'first_name':
                userFirstName=userData_Values['first_name']
            if key == 'last_name':
                userLastName = userData_Values['last_name']
            if key == 'email':
             userEmail = userData_Values['email']

    return render_template('assignment4_outer_source.html',userFirstName=userFirstName,userLastName=userLastName
                            ,picture=picture, userEmail=userEmail)




@assignment_4.route('/assignment4/restapi_users', defaults={'USER_ID': 319145959})
@assignment_4.route('/assignment4/restapi_users/<int:USER_ID>')
def restapi_func(USER_ID):
    if USER_ID==319145959:
        query = "select * FROM users WHERE user_ID='319145959';"
        users_list = app.interact_db(query, query_type='fetch')
        response = users_list[0]
        response = jsonify(response)
        return response


    query = "select * FROM users WHERE user_ID='%s';" % USER_ID
    users_list = app.interact_db(query, query_type='fetch')

    if len(users_list) != 0:
            response = users_list[0]
    else:
        response={
        'success': False,
        'error':'ID does not exist in the system'
        }
    response = jsonify(response)
    return response