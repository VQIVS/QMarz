from app import db

class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True,  nullable=False)
    tel_id = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return self.name 

