from app import db

class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    author = db.Column(db.String(100), nullable=False)
    
    content = db.Column(db.Text, nullable=False)
    
    # Updated: Default is False because new notes are active
    
    is_deleted = db.Column(db.Boolean, default=False) 

    def __repr__(self):
        return f'<Note {self.id} by {self.author}>'