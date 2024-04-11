from app import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __repr__(self):
        return f"<Movie {self.title}>"

