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

	if user_name=="":
		error = "Please enter your user_name."
		return redirect("/?error=" + error)	

	
	elif pass1 == pass2:
		return render_template('confirmation.html', user=user_name)	
	
	else:
		error = "Please confirm password."
		return redirect("/?error2=" + error)
	

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html',error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
