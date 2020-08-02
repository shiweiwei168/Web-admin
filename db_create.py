from app import db
from app.models import Admin, User

db.create_all()

print("DB created.")
