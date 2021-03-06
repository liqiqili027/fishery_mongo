import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP
basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The MongoEngine connection string.
MONGODB_SETTINGS = {
    'DB': 'fishery',
    #'host': 'ec2-35-153-16-119.compute-1.amazonaws.com',
    'host': 'localhost',
    'port': 27017,
    'username':'fishery',
    'password':'fishery123'
}

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#------------------------------
# GLOBALS FOR APP Builder
#------------------------------
# Uncomment to setup Your App name
#APP_NAME = "My App Name"

# Uncomment to setup Setup an App icon
#APP_ICON = "static/img/logo.jpg"

#----------------------------------------------------
# AUTHENTICATION CONFIG
#----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
#AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
#AUTH_ROLE_PUBLIC = 'Public'

AUTH_ROLE_GUEST = 'Guest'
# Will allow user self registration
#AUTH_USER_REGISTRATION = True

# The default user self registration role
#AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
#AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
#OPENID_PROVIDERS = [
#    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
#LANGUAGES = {
#    'en': {'flag':'gb', 'name':'English'},
#    'pt': {'flag':'pt', 'name':'Portuguese'},
#    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
#    'es': {'flag':'es', 'name':'Spanish'},
#    'de': {'flag':'de', 'name':'German'},
#    'zh': {'flag':'cn', 'name':'Chinese'},
#    'ru': {'flag':'ru', 'name':'Russian'}
#}
#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)
APP_NAME = "Fishery"

#===============================================
# User Registration
#===============================================
AUTH_TYPE = 1 # Database Authentication
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Registered User'
# Config for Flask-WTF Recaptcha necessary for user registration
RECAPTCHA_PUBLIC_KEY = '6LfYQmUUAAAAAK3ddaSW9j_SqycU5_PCJ4E1KCwN'
RECAPTCHA_PRIVATE_KEY = '6LfYQmUUAAAAAPOHIevx1YAaaQZHuBeHUUm_7BIb'
# Config for Flask-Mail necessary for user registration
MAIL_PORT=25
MAIL_USE_SSL=False
MAIL_SERVER = 'smtpout.fiu.edu'
MAIL_USE_TLS = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'gomredsnapper@fiu.edu'

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
#APP_THEME = "bootstrap-theme.css"  # default bootstrap
#APP_THEME = "cerulean.css"
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"
#APP_THEME = "spacelab.css"
#APP_THEME = "united.css"
#APP_THEME = "yeti.css"
