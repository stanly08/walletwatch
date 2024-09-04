# Expense Tracker Project

This is a web-based expense tracker application built using Flask. Below is the project structure.

Technologies to Use
Frontend:

HTML, CSS, JavaScript: Basic building blocks for creating the user interface.
Bootstrap or Tailwind CSS: For styling the application with a responsive design framework.
Backend:

Flask or Django (Python): you can use Python frameworks to build the backend.
User Authentication: Flask-Security (for Flask).
Database:

SQL (MySQL): For relational data storage, handling user accounts, and storing expenses.

Hosting/Deployment:

Heroku or Vercel: For deploying the web application with continuous integration and delivery.
AWS or DigitalOcean: For more customizable hosting options.

## Project Structure

```
walletwatch/
│
├── app.py				#main flask app
├── templates/				#html templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/				#css styles
│   ├── css/
│   │   └── styles.css
│   └── js/				#javascript files
│       └── scripts.js
├── models.py				#database models
├── forms.py				#form validation
└── expense_tracker.db			#SQLite or SQLAlchemy database

