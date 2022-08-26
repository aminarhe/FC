from flask import Flask, jsonify, request, render_template, redirect, url_for, session, abort
from database.db import execute
import datetime



app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = 'pASM:SCLVKJ:BNL$IGI&fsegdrhtfjy$#HRFLBGEIG'
app.permanent_session_lifetime = datetime.timedelta(days = 7)



def isLogged(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        return abort(401)
    else:
        return True


@app.route('/')
def landing():
    return redirect("/signup")
    return render_template("landing.html")


@app.route('/home/<username>')
def home(username):
    isLogged(username)
    return render_template(
        "home.html", 
        title = "Home", 
        username = username
    )


@app.route('/profile/<username>')
def profile(username):
    isLogged(username)
    return render_template(
        "profile.html", 
        title = "Profile", 
        username = username
    )


@app.route('/<username>/courses/js')
def course(username):
    isLogged(username)
    course = "js"
    level = 1
    return redirect("https://funcode-game.herokuapp.com/")
    return render_template(
        "course.html", 
        title = "JS", 
        username = username, 
        course = course, 
        level = level
    )


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    email    = request.form.get('email')
    password = request.form.get('password')

    if 'userLogged' in session:
        return redirect(url_for(
            'home', 
            username = session['userLogged']
        ))

    elif email is not None and password is not None:
        response = execute(f"""
            SELECT * FROM funcode_users 
            WHERE email = '{email}' and password = '{password}';
        """)

        if response['status'] == 'ok':
            if len(response['data']) > 0:
                session['userLogged'] = email
                return redirect(url_for(
                    'home', 
                    title = "Home", 
                    username = session['userLogged']
                ))
            else:
                return jsonify('The username or password you entered is incorrect. Try entering it again.')
        else:
            return jsonify('Server error')

    return render_template(
        "signin.html", 
        title = 'Sign in'
    )


@app.route('/logout/<username>')
def logout(username):
    isLogged(username)
    del session["userLogged"]
    return redirect(url_for('signin'))



@app.route('/signup', methods=['POST', 'GET'])
def signup():
    email     = request.form.get('email')
    password  = request.form.get('password')

    if 'userLogged' in session:
        return redirect(url_for(
            'home', 
            username = session['userLogged']
        ))

    elif email is not None and  password is not None:
        response = execute(f"SELECT * FROM funcode_users WHERE email = '{email}';")

        if response['status'] == 'ok' and len(response['data']) == 0:
            response = execute(f"""
                INSERT INTO funcode_users (email, password) 
                VALUES ('{email}', '{password}');
            """)

            if response['status'] == 'ok':
                session['userLogged'] = email
                return redirect(url_for(
                    'home', 
                    title = "Home", 
                    username = session['userLogged']
                ))

    return render_template(
        "signup.html", 
        title = "Sign up"
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)