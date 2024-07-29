from app import db
from datetime import datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Pending")

    def __repr__(self):
        return f"Order('{self.id}', '{self.date_ordered}', '{self.status}')"
