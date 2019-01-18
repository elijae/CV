from flask import Flask, request, render_template
import json

server = Flask(__name__)
attendentees = []


@server.route('/guests', methods=["GET"])
def just_list():
	return json.dumps(attendentees)

@server.route('/register', methods=["GET"])
def add():
	return render_template('capture.html')

@server.route('/guests', methods=["POST"])
def add_guests():
	name = request.form['name']
	amount = request.form['amount']
	attendentees.append({'name':name, 'amount':amount})
	return json.dumps(attendentees)


# elijejacob1026
server.run()