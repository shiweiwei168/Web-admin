from app import db
from app.models import Admin, Customer

db.create_all()

print("DB created.")
