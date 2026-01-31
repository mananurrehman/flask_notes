from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Note
from app import db

# create blueprint named 'main'

bp = Blueprint('main', __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get data from the form (author name and notes)
        author_val = request.form.get('author')
        content_val = request.form.get('content')

        new_note = Note(author=author_val, content=content_val)
        #create a new object using our Model

        #add it to the database session and save it
        db.session.add(new_note)
        db.session.commit()

        #after saving, stay on home page (or clear the form)
        return redirect(url_for('main.index'))
    
    return render_template("base.html")

# view notes 

@bp.route("/notes", methods=['GET', 'POST'])
def view_notes():
    notes = None
    search_performed = False
    author_name = request.args.get('search_author', "") # Check if redirected from delete

    if request.method == 'POST' or author_name:
        search_performed = True
        if not author_name:
            author_name = request.form.get('author_search')
        notes = Note.query.filter_by(author=author_name).all()

    return render_template("notes.html", notes=notes, search_performed=search_performed, author_name=author_name)


# ==> Trash (Deleted Notes)
@bp.route("/delete-note/<int:note_id>", methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    # Switch the status
    note.is_deleted = True
    db.session.commit()
    
    # We need to redirect back to the notes page. 
    # To keep the search results, we pass the author name back in the URL
    author_name = request.form.get('author_name')
    return redirect(url_for('main.view_notes', search_author=author_name))