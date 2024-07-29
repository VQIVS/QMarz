from app.models.tutorial import Tutorial
from app import db

class TutorialRepository:
    def get_all(self):
        try:

            tutorials = Tutorial.query.all()
            return tutorials
        
        except Exception as e:
            print(f"Error fetching all tutorials: {e}")
            return None
        
    def get_by_name(self, name):
        try:
            
            tutorial = Tutorial.query.filter_by(name=name).first()
            return tutorial
        
        except Exception as e:
            print(f"Error fetching tutorial by name: {e}")
            return None