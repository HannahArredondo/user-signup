from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/confirmation", methods=['POST'])
def confirmation():
    # look inside the request to figure out what the user typed
	user_name = request.form['username']
	pass1 = request.form['password1']
	pass2 = request.form['password2']
	
	user_error=""
	password1_error=""
	password2_error=""
	check = [user_name, pass1, pass2]

	for thing in check:
		if len(user_name) < 3 or " " in user_name:
			user_error = "Invalid Username"
		else:
			error = ""
			
	for thing in check:
		if  " " in pass1 or len(pass1) < 3:
			password1_error = "Invalid password"
		else:
			error = ""
	
	for thing in check:
		if pass1 != pass2:
			password2_error = "Passwords must match"
		else:
			error = ""
	
	
	if not user_error and not password1_error and not password2_error:
		return render_template('confirmation.html', user_name = user_name)
	
	else:
		return render_template('edit.html', user_name = user_name, user_error=user_error,
		password1_error=password1_error, password2_error=password2_error)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html',error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
