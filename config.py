import os

#.............................................
# Database configuration
#.............................................
# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<db_user>:<db_password>@<endpoint>/<db_url>'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

def getDBURI(filePath):
	if 'RDS_HOSTNAME' in os.environ:
		print "...in AWS branch of config.py.getDBURI()....."
		DATABASE = {	'ENGINE': 'mysql+pymysql',
				'NAME': os.environ['RDS_DB_NAME'],
				'USER': os.environ['RDS_USERNAME'],
				'PASSWORD': os.environ['RDS_PASSWORD'],
				'HOST': os.environ['RDS_HOSTNAME'],
				'PORT': os.environ['RDS_PORT']
		}

		#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<db_user>:<db_password>@<endpoint>/<db_url>'
		SQLALCHEMY_DATABASE_URI = "%(ENGINE)s://%(USER)s:%(PASSWORD)s@%(HOST)s/%(NAME)s" % DATABASE
	else:
		print "...in local branch in config.py.getDBURI()....."
		# filePath Global defined below
		file = open(DBFILEPATH, "r")
		SQLALCHEMY_DATABASE_URI = file.read()
	
	print "...SQLALCHEMY_DATABASE_URI : "
	print SQLALCHEMY_DATABASE_URI
	return SQLALCHEMY_DATABASE_URI

DBFILEPATH = "./.gitIgnored/SQLALCHEMY_DATABASE_URI.txt"

def getFakeDBURI():
	DATABASE = {	'ENGINE': 'mysql+pymysql',
					'NAME': 'RDS_DB_NAME',
					'USER': 'RDS_USERNAME',
					'PASSWORD': 'RDS_PASSWORD',
					'HOST': 'RDS_HOSTNAME',
					'PORT': 'RDS_PORT'
			}
	SQLALCHEMY_DATABASE_URI = "%(ENGINE)s://%(USER)s:%(PASSWORD)s@%(HOST)s/%(NAME)s" % DATABASE
	return SQLALCHEMY_DATABASE_URI
	
# tables to be created in the database
TABLES = [{'tableName':'users', 'columns':[
							{'name':'id', 'type':'Integer', 'other':', primary_key=True'},
							{'name':'social_id', 'type':'Integer', 'other':', nullable=True'},
							{'name':'name', 'type':'String(250)', 'other':', nullable=False'},
							{'name':'email', 'type':'String(250)', 'other':', nullable=False'},
							{'name':'password', 'type':'String(250)', 'other':', nullable=False'}
							]},
			{'tableName':'messsages', 'columns':[
							{'name':'id', 'type':'Integer', 'other':', primary_key=True'},
							{'name':'title', 'type':'String(250)', 'other':', nullable=False'},
							{'name':'text', 'type':'String(250)', 'other':', nullable=False'}
							]},
			{'tableName':'inventory', 'columns':[
							{'name':'id', 'type':'Integer', 'other':', primary_key=True'},
							{'name':'name', 'type':'String(250)', 'other':', nullable=False'},
							{'name':'description', 'type':'String(250)', 'other':', nullable=False'},
							{'name':'price', 'type':'Integer', 'other':', nullable=False'},
							{'name':'quantityAvailable', 'type':'Integer', 'other':', nullable=False'}
							]},
			{'tableName':'users', 'columns':[
							{'name':'id', 'type':'Integer', 'other':', primary_key=True'},
							{'name':'user_id', 'type':'Integer', 'other':', db.ForeignKey("users.id")'},
							{'name':'item_id', 'type':'Integer', 'other':', db.ForeignKey("inventory.id")'},
							{'name':'price', 'type':'Integer', 'other':', nullable=False'},
							{'name':'quantityOrdered', 'type':'Integer', 'other':', nullable=False'}
							]}
			]

#.............................................
# Oauth2 configuration
#.............................................

GOOGLE_LOGIN_CLIENT_ID = "<your-id-ending-with>/apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "<your-secret>"

OAUTH_CREDENTIALS={
		'google': {
			'id': GOOGLE_LOGIN_CLIENT_ID,
			'secret': GOOGLE_LOGIN_CLIENT_SECRET
		}
}

#.............................................
# Customer specific pages
#.............................................

SCREENS_IN_APP = {
		'donate': 'Donate',
		'messages': 'News',
		'contactus': 'Get in touch',
		'order': 'Buy Merch',
		'login': 'Log In'
		}
	
TEMPLATES = ["about","donate","hikerinfo","login","messages", "order", "settings", "tests", "updateinventory", "visit", "welcome"]
	
#.............................................
# Other things
#.............................................

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'