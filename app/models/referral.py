from app import db


class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.String(128), nullable=False)
    referred_id = db.Column(db.String(128), nullable=False)

    def __init__(self, referrer_id, referred_id):
        self.referrer_id = referrer_id
        self.referred_id = referred_id
