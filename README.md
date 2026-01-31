# Flask Note Manager

A clean, modular web application built with Python and Flask that allows users to save notes, search for notes by author, and perform "soft deletes" on existing records. 

## 🚀 Features
- **Add Notes**: Users can submit notes with an author name and content.
- **Search Filtering**: View notes specifically filtered by author name.
- **Soft Delete**: Mark notes for deletion with a visual "Trash" status before permanent removal.
- **Responsive Design**: Styled with Tailwind CSS for a modern look.
- **PostgreSQL Database**: Persistent storage using SQLAlchemy ORM.
- **Factory Pattern**: Professional folder structure for better scalability.

---

## 📸 Screenshots

### 1. Home - Add Note Form
![Add Note Page](path_to_your_screenshot1.png)
*The main landing page where users can input their notes and author details.*

### 2. Search Page
![Search Page](path_to_your_screenshot2.png)
*The interface where users enter an author's name to filter the database.*

### 3. View & Delete Notes
![Notes View](path_to_your_screenshot3.png)
*The results display featuring the "Soft Delete" highlight for marked notes.*

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **ORM:** Flask-SQLAlchemy
- **Migrations:** Flask-Migrate
- **Frontend:** HTML5, Jinja2, Tailwind CSS

---

## ⚙️ Installation & Setup

1. **Clone the project**
   ```bash
   git clone <your-repo-link>
   cd flask_notes

2. **Create and Activate Virtual Environment**
    python -m venv venv
    .\venv\Scripts\activate

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Database Configuration**
    Update the 'SQLALCHEMY_DATABASE_URI' in *config.py* with your PostgreSQL credentials.

5. **Run Migrations**
    flask db init
    flask db migrate -m "initial setup"
    flask db upgrade

6. **Run the Application**
    python run.py

---

## 📂 Project Structure

```text
flask_notes/
│
├── venv/                 # Virtual environment
├── app/                  # Application package
│   ├── __init__.py       # App factory & extension init
│   ├── models.py         # SQLAlchemy models (Note)
│   ├── routes.py         # Routes using 'bp' Blueprint
│   └── templates/        # Jinja2 HTML templates
│       ├── base.html     # Add note form
│       └── notes.html    # Search & View notes
├── migrations/           # Database migration scripts
├── config.py             # Database & Secret Key config
├── run.py                # App entry point
├── .flaskenv             # Flask environment variables
└── requirements.txt      # Project dependencies