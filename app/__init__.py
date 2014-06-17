from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import signal

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import Match
from app.routes import index

from app.routes import Matches

from app.lib.WCGaugeStream import WCGaugeStream


wcgs = WCGaugeStream()
def handleCtrlC():
    wcgs.stopStream()
signal.signal(signal.SIGINT, handleCtrlC)