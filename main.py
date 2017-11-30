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

	if len(user_name) < 3:
		error = "Invalid Username"
		return render_template('edit.html', user_name=user_name, error= error)
	
	elif " " in user_name:
		error = "Invalid Username no space allowed!"
		return render_template('edit.html', user_name=user_name, error= error)
		
	elif " " in pass1 or len(pass1) < 3:
		error = "Invalid password"
		return render_template('edit.html', user_name=user_name, error= error)
	
	elif pass1 != pass2:
		error = "Passwords must match"
		return render_template('edit.html', user_name=user_name, error= error)

	else:
		return render_template('confirmation.html', user=user_name)
	

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html',error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
