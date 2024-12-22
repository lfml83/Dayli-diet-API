from database import db
from sqlalchemy.sql import func 

class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(80),nullable=True)
    date_time = db.Column(db.DateTime(timezone=True), default=func.now())
    inside_outside = db.Column(db.Boolean, default=True)

