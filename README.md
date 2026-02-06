# 🔗 LinkUp

**LinkUp** is a Facebook-inspired social media platform built with
**Django**, designed with a strong focus on backend architecture, clean
data modeling, and real-world social features.

This project is built as a **backend-first learning application** and
serves as a solid foundation for future migration to **Django Rest
Framework (DRF)**.

------------------------------------------------------------------------

## 🚀 Features

### ✅ Implemented Features

-   [x] Custom User model (email-based authentication)
-   [x] User registration (signup)
-   [x] User login & logout
-   [x] Automatic profile creation on signup
-   [x] User profile pages
-   [x] Edit profile (bio, profile picture, cover picture, location)
-   [x] Create posts (text + optional image)
-   [x] Like / Unlike posts
-   [x] Comment on posts
-   [x] Follow / Unfollow users
-   [x] Personalized feed (self + followed users)
-   [x] Paginated feed
-   [x] Function-based views across the project
-   [x] Clean app-based architecture

------------------------------------------------------------------------

## 🧭 Future Roadmap

-   [ ] Post & comment deletion with ownership checks
-   [ ] Notifications system (likes, comments, follows)
-   [ ] Search users and posts
-   [ ] AJAX-based interactions (no page reloads)
-   [ ] Saved posts / bookmarks
-   [ ] Hashtags & trending posts
-   [ ] User blocking and reporting
-   [ ] Password reset via email
-   [ ] Email verification
-   [ ] REST API using Django Rest Framework (DRF)
-   [ ] Automated tests
-   [ ] Production deployment (Docker / Railway / Render)

------------------------------------------------------------------------

## 🏗️ Tech Stack

-   **Backend:** Django
-   **Database:** SQLite (development)
-   **Authentication:** Django Auth (custom User model)
-   **Templates:** Django Templates
-   **Frontend:** Minimal HTML (backend-focused)

------------------------------------------------------------------------

## 📂 Project Structure

    linkup/
    ├── accounts/        # authentication & custom user
    ├── profiles/        # user profiles
    ├── posts/           # posts, likes, comments
    ├── follows/         # follow system
    ├── core/            # feed & homepage logic
    ├── templates/       # global templates
    ├── static/          # static files
    ├── media/           # user uploads
    └── manage.py

------------------------------------------------------------------------

## ⚙️ Installation Guide

### 1️⃣ Clone the repository

    git clone https://github.com/your-username/linkup.git
    cd linkup

### 2️⃣ Create and activate virtual environment

    python -m venv venv

**Windows**

    venv\Scripts\activate

**Mac / Linux**

    source venv/bin/activate

------------------------------------------------------------------------

### 3️⃣ Install dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

### 4️⃣ Apply migrations

    python manage.py makemigrations
    python manage.py migrate

------------------------------------------------------------------------

### 5️⃣ Create superuser (optional)

    python manage.py createsuperuser

------------------------------------------------------------------------

### 6️⃣ Run development server

    python manage.py runserver

Open in browser:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🧠 Learning Objectives

-   Master Django app-based architecture
-   Design scalable database relationships
-   Implement social media feed logic
-   Gain deep understanding of function-based views
-   Build a strong base for DRF and API development

------------------------------------------------------------------------

## 📌 Notes

-   This project intentionally avoids DRF initially to strengthen Django
    fundamentals
-   Emphasis is on backend design, performance, and scalability
-   UI is intentionally minimal

------------------------------------------------------------------------

## 👨‍💻 Author

Built as a backend-focused learning project using Django.
