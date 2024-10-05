from market import app, db
app.app_context().push()
db.create_all()
from market.models import Item,User

user1 = User(username="rbcadaing",email_address="rbcadaing@gmail.com",password_hash="kjdjhld",budget=123)
db.session.add(user1)
db.session.commit()

item1 = Item(name="Iphone 10",price=200,barcode='0987303',description='mobile')
item1.owner = User.query.filter_by(username='rbcadaing').first().id
db.session.add(item1)
db.session.commit()

item2 = Item(name="Laptop",price=700,barcode='209862',description='laptop')
item2.owner = User.query.filter_by(username='rbcadaing').first().id
db.session.add(item2)
db.session.commit()

Item.query.all()