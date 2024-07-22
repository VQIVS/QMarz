from app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    orders = db.relationship("Order", backref="subscription", lazy=True, cascade="all, delete-orphan")
    

    def __repr__(self):
        return f"Subscription('{self.plan}', '{self.price}', '{self.duration_months} months')"
