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