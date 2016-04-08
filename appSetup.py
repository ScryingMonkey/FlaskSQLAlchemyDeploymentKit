import os
from config import TEMPLATES, TABLES

def createApplicationFile(listOfTemplates):
	imports = ''
	imports += 'from flask import Flask, render_template, request, redirect,jsonify, url_for, flash\n'
	imports += 'from flask.ext.login import login_user, logout_user, current_user, login_required\n'
	imports += 'from application.models import Data, Users, Questions, Results\n'
	imports += 'from application.forms import EnterDBInfo, RetrieveDBInfo\n'
	imports += 'from application.logic import *\n'
	imports += 'from flask import session as login_session\n'
	imports += 'from flask import make_response\n'
	imports += 'import random, string\n'
	imports += 'from oauth2client.client import flow_from_clientsecrets, FlowExchangeError\n'
	imports += 'import httplib2\n'
	imports += 'import json\n'
	imports += 'import requests\n'
	imports += 'from application import db\n'
	imports += 'import random\n'
	imports += '\n'
	
	topBoilerPlate = ''
	topBoilerPlate += '# Elastic Beanstalk initalization\n'
	topBoilerPlate += 'application = Flask(__name__)\n'
	topBoilerPlate += 'application.debug=True\n'
	topBoilerPlate += '# change this to application specific key\n'
	topBoilerPlate += 'application.secret_key = "cC1YCIWOj9GgWspgNEo2"\n'

	getBoilerPlate = ''
	getBoilerPlate += '#..............................................................................................\n'
	getBoilerPlate += '#.....GET Requests.............................................................................\n'
	getBoilerPlate += '#..............................................................................................\n'
	getBoilerPlate += '\n'

	postBoilerPlate = ''
	postBoilerPlate += '#.............................................................................................\n'
	postBoilerPlate += '#.....POST Requests.............................................................................\n'
	postBoilerPlate += '#.............................................................................................\n'
	postBoilerPlate += '\n'
	postBoilerPlate += '# Login page\n'
	postBoilerPlate += '@application.route("/login", methods=["GET", "POST"])\n'
	postBoilerPlate += 'def login():\n'
	postBoilerPlate += '	if g.user is not None and g.user.is_authenticated():\n'
	postBoilerPlate += '		return redirect(url_for("index"))\n'
	postBoilerPlate += '	return render_template("login.html",\n'
	postBoilerPlate += '						   title="Sign In")\n'
	postBoilerPlate += '\n'

	helperBoilerPlate = ''
	helperBoilerPlate += '#.............................................................................................\n'
	helperBoilerPlate += '#.....Helper requests.............................................................................\n'
	helperBoilerPlate += '#.............................................................................................\n'
	helperBoilerPlate += '@application.route("/authorize/<provider>")\n'
	helperBoilerPlate += 'def oauth_authorize(provider):\n'
	helperBoilerPlate += '	# Flask-Login function\n'
	helperBoilerPlate += '	if not current_user.is_anonymous():\n'
	helperBoilerPlate += '		return redirect(url_for("index"))\n'
	helperBoilerPlate += '	oauth = OAuthSignIn.get_provider(provider)\n'
	helperBoilerPlate += '	return oauth.authorize()\n'
	helperBoilerPlate += '	@application.route("/callback/<provider>")\n'
	helperBoilerPlate += '\n'
	helperBoilerPlate += 'def oauth_callback(provider):\n'
	helperBoilerPlate += '	if not current_user.is_anonymous():\n'
	helperBoilerPlate += '		return redirect(url_for("index"))\n'
	helperBoilerPlate += '	oauth = OAuthSignIn.get_provider(provider)\n'
	helperBoilerPlate += '	username, email = oauth.callback()\n'
	helperBoilerPlate += '	if email is None:\n'
	helperBoilerPlate += '		# I need a valid email address for my user identification\n'
	helperBoilerPlate += '		flash("Authentication failed.")\n'
	helperBoilerPlate += '		return redirect(url_for("index"))\n'
	helperBoilerPlate += '	# Look if the user already exists\n'
	helperBoilerPlate += '	user=User.query.filter_by(email=email).first()\n'
	helperBoilerPlate += '	if not user:\n'
	helperBoilerPlate += '		# Create the user. Try and use their name returned by Google,\n'
	helperBoilerPlate += '		# but if it is not set, split the email address at the @.\n'
	helperBoilerPlate += '		nickname = username\n'
	helperBoilerPlate += '		if nickname is None or nickname == "":\n'
	helperBoilerPlate += '			nickname = email.split("@")[0]\n'
	helperBoilerPlate += '\n'
	helperBoilerPlate += '		# We can do more work here to ensure a unique nickname, if you \n'
	helperBoilerPlate += '		# require that.\n'
	helperBoilerPlate += '		user=User(nickname=nickname, email=email)\n'
	helperBoilerPlate += '		db.session.add(user)\n'
	helperBoilerPlate += '		db.session.commit()\n'
	helperBoilerPlate += '	# Log in the user, by default remembering them for their next visit\n'
	helperBoilerPlate += '	# unless they log out.\n'
	helperBoilerPlate += '	login_user(user, remember=True)\n'
	helperBoilerPlate += '	return redirect(url_for("index"))\n'
	helperBoilerPlate += '\n'

	bottomBoilerPlate = "\n"
	bottomBoilerPlate += "#..............................................................................................\n"
	bottomBoilerPlate += "#.....Boiler plate.............................................................................\n"
	bottomBoilerPlate += "#..............................................................................................\n"
	bottomBoilerPlate += "if __name__ == '__main__':\n"
	bottomBoilerPlate += "	#application.run(host='0.0.0.0')<---works on aws eb\n"
	bottomBoilerPlate += "	application.run(host = '0.0.0.0', port = 5000)\n"

	for t in listOfTemplates:
		route = ""
		route += "# %s page\n" % t
		route += "@application.route('/%s', methods=['GET'])\n" % t
		route += "def %s():\n" % t
		route += "	return render_template('%s.html')\n" % t
		route += "\n"
#		print route
		getBoilerPlate += route

	content = [imports, topBoilerPlate, getBoilerPlate, postBoilerPlate, helperBoilerPlate, bottomBoilerPlate]
	createFile("application.py", content)

def createTemplates(listOfTemplates):
	directory = "templates"
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	content = ''
	content += '{% extends "main.html" %}\n'
	content += '{% block content %}\n'
	content += '{% include "header.html" %}\n'
	content += '\n'
	content += '\n'
	content += '\n'
	content += '{% include "footer.html" %}\n'
	content += '{% endblock %}\n'

	for t in listOfTemplates:
		fileName = "%s/%s.html" % (directory,t)
		createFile(fileName, content)

def createIgnoredFolders():
	ignoredFolders = [".ebextensions", ".elasticbeanstalk", ".git", ".gitIgnored", ".vagrant"]
	for f in ignoredFolders:
		if not os.path.exists(f):
			os.makedirs(f)
		fileName = '%s/.gitignore' % f
		createFile(fileName, "[^.]*")
	createFile(".gitIgnored/SQLALCHEMY_DATABASE_URI.txt", "Replace this with database URL")

def createDBFiles(tables):
	imports = ''
	imports += 'from application import db\n'
	imports += '\n'
	imports += '\n'
	
	tablesContent = ''
								
	for t in tables:
		Name = t['tableName'].capitalize()
		table = ''
		table += '# Define %s table..................................................\n' % Name
		table += 'class %s(db.Model)\n' % Name
		# define Columns
		for r in t['columns']:
			print "...r : %s" % r
			table += '	%s = db.Column(db.%s%s)\n' % (r['name'], r['type'], r['other'])
		print "...t['columns'][-1] : %s" % t['columns'][-1]
		table += '\n'
		# def __init__
		table += '	def __init__(self, name, email, password):\n'
		for r in t['columns']:
			if "id" in r['name']:
				continue
			else:
				table += '		self.%s = %s\n' % (r['name'],r['name'])
		table += '\n'
		# def __repr__
		table += '	def __repr__(self):\n'
		table += '		return "<%s %s>" %s self.name\n' % (Name, '%r', '%')
		table += '\n'
		# def serialize
		table += '	@property\n'
		table += '	def serialize(self):\n'
		table += '		"""Return object data in easily serializeable format"""\n'
		table += '		return {\n'
		for r in t['columns'][:-1]:
			if 'password' not in r['name']:
				table += '			"%s"			: self.%s,\n' % (r['name'], r['name'])
		if 'password' not in t['columns'][-1]['name']:
			table += '			"%s"			: self.%s\n' % (t['columns'][-1]['name'], t['columns'][-1]['name'])
		table += '		}\n'
		table += '\n'
		print table
		tablesContent += table
		
	content = imports, tablesContent
	directory = "application"
	if not os.path.exists(directory):
			os.makedirs(directory)
	fileName = '%s/%s' % (directory, 'models.py')
	createFile(fileName, content)
	
def createFile(fileName, content):
	print "...Creating file: %s" % fileName
	file = open(fileName, "w")
	text = ""
	for e in content:
		text = text + e
	file.write(text)
	file.close()
	print "...file created"


	
createIgnoredFolders()
# TEMPLATES from config.py
createApplicationFile(TEMPLATES)
createTemplates(TEMPLATES)
# TABLES from config.py
createDBFiles(TABLES)