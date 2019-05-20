from flask import *
from functools import wraps
from mongo import connect

#from mongo import connect
from flask_session import Session
import datetime
#from config import conf

from logging.handlers import RotatingFileHandler
from functools import wraps
import logging

app = Flask(__name__)
app.secret_key = 'token'
app.config['ASK_VERIFY_REQUESTS'] = False
#db = connect();

app.config['SESSION_PERMANENT'] = True
app.permanent_session_lifetime = datetime.timedelta(seconds=60*60)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

from .index import *
from .issuer_issuing import *
from .user_issuing import *
from .verifying import *