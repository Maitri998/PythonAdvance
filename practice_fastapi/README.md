#  FastAPI User Authentication API

This is a simple user authentication system built using **FastAPI**, **SQLite**, and **JWT (JSON Web Tokens)**. It provides user registration, login, and authenticated access to user management endpoints. The Swagger UI includes an **Authorize** button for easy token handling.

---

## Features

- User registration with hashed passwords
- JWT-based login and authentication
- Token validation middleware
- Protected CRUD operations for users
- SQLite database (lightweight and file-based)
- Swagger UI with built-in "Authorize" support

---

## Tech Stack

- **FastAPI** – Web framework
- **SQLite** – Lightweight embedded database
- **PyJWT or python-jose** – JWT encoding/decoding
- **Pydantic** – Data validation

---

##  Installation

1. Clone the repository

```bash
git clone https://github.com/Maitri998/PythonAdvance.git
cd PythonAdvance/practice_fastapi

2. Install Dependencies
pip install requirements.txt

3. Run the Application
uvicorn main:app --reload

4.  Using the Authorize Button in Swagger
First, register and login to get your JWT token.

Click the "Authorize" button at the top of Swagger UI.

5. Protected Endpoints (require JWT)
----Get All Users
GET /users
Headers:
Authorization: Bearer <token>
Update User
PUT /users/{user_id}

Delete User
DELETE /users/{user_id}

6.API Documentation
Once the app is running, open your browser to:

Swagger UI: http://127.0.0.1:8000/docs

7. Project Structure

.
├── main.py          # FastAPI routes
├── auth.py          # JWT authentication logic
├── models.py        # DB operations (SQLite)
├── database.py      # DB connection + setup
├── schemas.py       # Pydantic models
├── utils.py         # Token creation, password hashing
└── README.md
