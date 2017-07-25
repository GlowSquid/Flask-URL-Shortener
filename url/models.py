import datetime
from app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old = db.Column(db.String(255))
    new = db.Column(db.String(5), unique=True)
    active = db.Column(db.Boolean, default=True)
    hits = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super(Url, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<URL %s>' % self.old
