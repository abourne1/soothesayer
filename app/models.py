from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    texts = db.relationship('Post', backref='author', lazy='dynamic')
    phone_number = db.Column(db.String(20))
    other_number = db.Column(db.String(20))

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    from_number = db.Column(db.String(20))
    to_number = db.Column(db.String(20))
    tag = db.Column(db.Integer)

    def __repr__(self):
        return '<Post %r>' % (self.body)