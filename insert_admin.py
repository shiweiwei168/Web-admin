from app import app, db
from app.models import Admin,Customer

#insert a default admin into the database  
admin = Admin(username='admin',email='admin@stateform.com',phone='6667778888',department='IT',usertype=1)
admin.set_password('admin')
db.session.add(admin)
db.session.commit()

#insert records into customer to test the system. will be remove before the deployment.
user = Customer(username='weishi',fname='Wei',lname='Shi',gender =1, city ='Arlington',score=630, email='shiweiwei@gmail.com',phone='6667778888')
db.session.add(user)
db.session.commit()
user = Customer(username='linus', fname='linus',lname='Torvalds',gender =1, city ='Fort Worth',score=900, email='linux@gmail.com',phone='1112223333')
db.session.add(user)
db.session.commit()
user = Customer(username= 'dalio', fname='Brian',lname='Dalio',gender =1, city ='Keller',score=800, email='Dalio@gmail.com',phone='1112225555')
db.session.add(user)
db.session.commit()

