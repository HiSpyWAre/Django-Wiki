# 🧭 Django Wiki Project

A simple encyclopedia web application built with **Django** (Python) as part of *CS50’s Web Programming with Python and JavaScript*.  
This project allows users to view, search, create, edit, and explore pages written in Markdown format.

---
## 🚀 Features

- 📄 Display encyclopedia entries written in Markdown  
- 🔍 Search for entries by title or keyword  
- ✏️ Create new pages through a web form  
- 🪄 Edit existing pages directly from the browser  
- 🎲 View a random entry  
- 🧱 Markdown rendered to HTML dynamically  

---
## 🗂️ Project Structure

wiki/
├── encyclopedia/
│ ├── static/encyclopedia/styles.css
│ ├── templates/encyclopedia/
│ │ ├── index.html
│ │ ├── entry.html
│ │ ├── new.html
│ │ ├── edit.html
│ │ ├── search.html
│ │ └── notfound.html
│ ├── urls.py
│ ├── views.py
│ ├── util.py
│ ├── models.py
│ └── init.py
│
├── entries/
│ ├── Python.md
│ ├── Git.md
│ ├── Django.md
│ ├── HTML.md
│ ├── CSS.md
│ └── Java.md
│
├── wiki/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
│ └── init.py
│
├── manage.py
└── README.md
