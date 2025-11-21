🌱 LearnLog — Track Your Learning Journey

A modern Django + POSTGRESQL web app that helps learners track, manage, and visualize their personal learning progress across books, courses, and tutorials.



🚀 Overview

LearnLog is your personal learning progress tracker, built for students, developers, and lifelong learners who want to organize what they’re studying — and see their growth in one place.
Users can add learning resources, update progress, and monitor completion stats — all through a clean, responsive dashboard.

✨ Features

✅ User Authentication


Secure sign-up and login system using Django’s built-in auth

Automatic redirect to dashboard after login


📚 Learning Resource Management


Add, view, and update your resources

Progress tracking from 0% to 100%

“Mark as Completed” action


📊 Dashboard Insights


Visual stats for total, completed, and in-progress resources

Auto-calculated average progress bar


🧭 Modern UI


Dynamic, mobile-friendly interface with smooth transitions

One-page authentication (toggle between login and signup)

POSTGRESQL hosted on render


Relational storage for user data and learning resources

Optimized queries for scalability


🧩 Tech Stack

Layer	Technology

Backend	Django (Python 3.x)

Frontend	HTML5, CSS3, JavaScript

Database	POSTGRESQL (Render)

Auth	Django’s built-in authentication system

Hosting (optional)	Render 

Version Control	Git + GitHub

🛠️ Installation & Setup

1. Clone the Repository
git clone https://github.com/yourusername/learnlog.git
cd learnlog

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root and add:

SECRET_KEY=your_django_secret_key

DEBUG=True

DATABASE_NAME=learn_db

DATABASE_USER=root

DATABASE_PASSWORD=your_password

DATABASE_HOST=localhost

DATABASE_PORT=3306


5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create Superuser
python manage.py createsuperuser

7. Run the Development Server
python manage.py runserver


Visit http://127.0.0.1:8000/
 to get started 🚀

🧠 Project Structure

learnlog/

├── manage.py

├── requirements.txt

├── .env

├── .gitignore

├── static/

│   ├── style.css

│   ├── main.js

│   └── learnlog.png

├── templates/

│   ├── index.html

│   ├── dashboard.html

│   ├── add-resource.html

│   └── resource-detail.html

├── learnlog_app/

│   ├── models.py

│   ├── views.py

│   ├── urls.py

│   └── forms.py


	
	
🧮 Database Model Overview

Resource

Field	Type	Description

title	CharField	Resource title

category	CharField	Book / Course / Tutorial

progress	IntegerField	Completion percentage

completed	BooleanField	True if finished

user	ForeignKey(User)	Resource owner

🧩 API Endpoints (Optional if you add APIs later)

Endpoint	Method	Description

/signup/	POST	Register new user

/login/	POST	Log user in

/dashboard/	GET	View learning stats

/add-resource/	POST	Add new resource

/resource-detail/?id=<id>	GET	View resource details


🤝 Contributing

Fork the repository

Create a new branch: git checkout -b feature-name

Commit changes: git commit -m "Add new feature"

Push and open a Pull Request

🛡️ Security

No credentials or secrets should ever be committed to Git.

Use environment variables for sensitive data (MySQL, secret key).


🧑‍💻 Author

Fadilah Abdulkadir

💼 Site Reliability Engineer | AWS Cloud Solutions Architect | Backend Developer | Python and Django

📧 [fadeelzy@gmail.com] 
🌐 [https://www.linkedin.com/in/fadilah-abdulkadir/]

📜 License

This project is licensed under the MIT License — feel free to use and modify it.



“Learning never exhausts the mind.” – Leonardo da Vinci
