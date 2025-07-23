# FastAPI Blog API Project Documentation

## Overview

This project is a RESTful API for a blog application built using FastAPI, SQLAlchemy, and PostgreSQL. It demonstrates modern Python web development practices, including authentication, ORM, and modular code organization.

---

## Project Structure

```
FastAPI-blog-api-project/
├── main.py                # FastAPI app entry point
├── requirements.txt       # Python dependencies
├── blog/
│   ├── database.py        # Database connection and session
│   ├── hashing.py         # Password hashing utilities
│   ├── models.py          # SQLAlchemy ORM models
│   ├── oauth2.py          # OAuth2 authentication logic
│   ├── schemas.py         # Pydantic schemas for validation/serialization
│   ├── token.py           # JWT token creation and verification
│   ├── repository/
│   │   ├── blog_repo.py   # Blog CRUD operations
│   │   └── user_repo.py   # User CRUD operations
│   └── routers/
│       ├── authentication.py # Login route
│       ├── blog.py            # Blog routes
│       └── user.py            # User routes
└── fastapienv/            # Python virtual environment
```

---

## Code Flow & Concepts

### 1. App Initialization (`main.py`)

- Creates a FastAPI app instance.
- Initializes database tables using SQLAlchemy.
- Includes routers for authentication, blog, and user endpoints.

### 2. Database Layer (`database.py`)

- Uses SQLAlchemy to connect to PostgreSQL.
- Provides a session generator (`get_db`) for dependency injection.

### 3. Models (`models.py`)

- Defines `User` and `Blog` ORM models with relationships.
- Each model maps to a database table.

### 4. Schemas (`schemas.py`)

- Uses Pydantic for data validation and serialization.
- Separates input schemas (for requests) and output schemas (for responses).
- `from_attributes=True` in `Config` allows Pydantic to work with ORM objects.

### 5. Password Hashing (`hashing.py`)

- Uses `passlib` with bcrypt for secure password storage.
- Provides methods to hash and verify passwords.

### 6. Authentication (`routers/authentication.py`, `oauth2.py`, `token.py`)

- Implements login with OAuth2 and JWT tokens.
- Validates user credentials and issues access tokens.
- Protects routes using dependency injection and token verification.

### 7. Routers (`routers/`)

- Organizes API endpoints by resource (blog, user, authentication).
- Uses FastAPI's `APIRouter` for modular route definitions.
- Injects dependencies (like DB session, current user) using `Depends`.

### 8. Repository Pattern (`repository/`)

- Separates business logic (CRUD operations) from route handlers.
- Improves code maintainability and testability.

---

## Example Request Flow

1. **User Registration**: `POST /user/`
   - Validates input with `User` schema.
   - Hashes password before storing.
   - Returns created user info.
2. **Login**: `POST /login`
   - Verifies credentials.
   - Returns JWT access token.
3. **Create Blog**: `POST /blog/`
   - Requires authentication (JWT token).
   - Associates blog with current user.
   - Returns created blog info.
4. **Get Blogs**: `GET /blog/`
   - Returns list of all blogs.
5. **Update/Delete Blog**: `PUT/DELETE /blog/{id}`
   - Allows modification/removal of blogs by ID.

---

## Key FastAPI Concepts Used

- **Dependency Injection**: `Depends` is used to inject DB sessions, current user, etc.
- **Pydantic Models**: For request/response validation and serialization.
- **APIRouter**: For modular route organization.
- **JWT Authentication**: Secure access to protected endpoints.
- **SQLAlchemy ORM**: For database modeling and queries.

---

## How FastAPI Works in This App

- FastAPI automatically validates and parses incoming requests using Pydantic schemas.
- Dependency injection simplifies resource management (DB sessions, authentication).
- Routers keep code modular and organized.
- SQLAlchemy handles database interactions, while Pydantic schemas ensure data integrity.
- JWT tokens provide stateless authentication for secure API access.

---

## Notes

- Always hash passwords before storing them.
- Use environment variables for sensitive info (like DB credentials, secret keys) in production.
- Modular code (routers, repositories) makes the app easier to maintain and extend.
- FastAPI's automatic docs (`/docs`) help with API exploration and testing.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Passlib Documentation](https://passlib.readthedocs.io/)
- [Python-Jose JWT](https://python-jose.readthedocs.io/)
