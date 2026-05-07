# User CRUD API

A simple and robust RESTful API for managing user information (name, email, and phone), built following **Clean Architecture** principles.

## 🚀 Features

- **CRUD Operations**: Create, Read (Single & All), Update, and Delete users.
- **Architecture**: Clean Architecture (Domain, Application, Infrastructure layers).
- **Tech Stack**:
  - **Python**: Core programming language.
  MT - **FastAPI**: High-performance web framework.
  - **Poetry**: Modern dependency management and packaging.
  - **In-Memory Repository**: Simple implementation for demonstration (easily replaceable with SQL via SQLAlchemy/Tortoise).
  - **Pydantic**: Data validation and settings management.

## 🛠️ Tech Stack & Tools

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Dependency Management**: [Poetry](https://python-poetry.org/)
- **Architecture Pattern**: Clean Architecture
- **Validation**: Pydantic

## 📋 Prerequisites

Ensure you have the following installed:
- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/flaviohbonfim/user-crud-api.git
   cd user-crud-api
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

## 🚀 Running the Application

To start the development server with auto-reload:

```bash
uvicorn src.infrastructure.api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/users/` | Create a new user |
| `GET` | `/users/` | Retrieve all users |
| `GET` | `/users/{user_id}` | Retrieve a specific user by ID |
| `PUT` | `/users/{user_id}` | Update an existing user |
| `DELETE` | `/users/{user <<user_id>>}` | Delete a user |

## 🏗️ Project Structure (Clean Architecture)

```text
src/
├── application/       # Use Cases and Repository Interfaces
│   ├── repositories/  # Abstract base classes for repos
│   └── use_cases/     # Business logic implementation
├── domain/            # Entities and Domain rules
│   └── entities.py    # Core User entity
└── infrastructure/    # External implementations
    ├── api/           # FastAPI routes, schemas, and entry point
    └── repositories/  # Concrete repository implementations (e.g., In-Memory)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
