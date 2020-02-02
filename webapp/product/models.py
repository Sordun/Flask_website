from webapp.db import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    kind = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Product {} {}>'.format(self.id, self.price)
