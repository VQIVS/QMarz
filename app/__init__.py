from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.models.user import User
        from app.models.order import Order
        from app.models.subscription import Subscription
        from app.models.tutorial import Tutorial


        db.create_all()

    return app
