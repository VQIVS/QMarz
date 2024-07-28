from app.models.subscription import Subscription
from app import db

class SubscriptionRepository:
    def create(self, plan, price, duration_days, user_id):
        new_subscription = Subscription(
            plan=plan,
            price=price,
            duration_days=duration_days,
            user_id=user_id
        )
        db.session.add(new_subscription)
        db.session.commit()
        return new_subscription
    
    def get_by_user_id(self, user_id):
        return Subscription.query.filter_by(user_id=user_id).all()