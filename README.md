# 📚 FastAPI Books Backend

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)

A modern, high-performance RESTful API for managing books, built with FastAPI.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Roadmap](#-roadmap)

</div>

---

## 🌟 Features

### Current Features
- ⚡ **High Performance**: Built on FastAPI for blazing-fast API responses
- 📖 **Book Management**: Complete CRUD operations for books
- 🔍 **Data Validation**: Automatic request/response validation with Pydantic
- 📝 **Interactive Documentation**: Auto-generated OpenAPI (Swagger) and ReDoc documentation
- 🎯 **Type Safety**: Full type hints for better IDE support and code quality

### Coming Soon
- 🔐 **JWT Authentication**: Secure user authentication and authorization
- ⚠️ **Error Middleware**: Comprehensive error handling and logging
- 👤 **User Management**: User registration, login, and profile management
- 🔒 **Role-Based Access Control**: Fine-grained permissions system
- 🗃️ **Database Integration**: PostgreSQL/MySQL support with SQLAlchemy ORM
- 📊 **Advanced Search**: Full-text search and filtering capabilities
- 🚀 **Rate Limiting**: API rate limiting to prevent abuse
- 📧 **Email Notifications**: Email integration for user notifications
- 🌐 **CORS Configuration**: Configurable CORS for frontend integration

---

## 🛠️ Technology Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- **Language**: [Python 3.8+](https://www.python.org/) - High-level programming language
- **Validation**: [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type annotations
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

### Upcoming Integrations
- **Database ORM**: SQLAlchemy
- **Database**: PostgreSQL / MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Migrations**: Alembic
- **Task Queue**: Celery (optional)
- **Caching**: Redis (optional)

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/huzipro/FastAPI-Books-Backend.git
cd FastAPI-Books-Backend
```

### 2. Create a Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Application Settings
APP_NAME=FastAPI Books Backend
APP_VERSION=1.0.0
DEBUG=True

# Server Configuration
HOST=0.0.0.0
PORT=8000

# Database Configuration (Coming Soon)
# DATABASE_URL=postgresql://user:password@localhost/books_db

# JWT Configuration (Coming Soon)
# SECRET_KEY=your-secret-key-here
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🎮 Usage

### Running the Application

#### Development Mode (with auto-reload)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at: `http://localhost:8000`

### Accessing Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 📚 API Documentation

### Base URL

```
http://localhost:8000/api/v1
```

### Endpoints Overview

#### Books

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/{id}` | Get a specific book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |

#### Example: Create a Book

```bash
curl -X POST "http://localhost:8000/api/v1/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "isbn": "978-0-7432-7356-5",
    "published_year": 1925,
    "description": "A classic American novel set in the Jazz Age"
  }'
```

#### Example: Get All Books

```bash
curl -X GET "http://localhost:8000/api/v1/books"
```

### Response Format

All API responses follow this format:

```json
{
  "success": true,
  "data": {},
  "message": "Operation successful"
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error description"
  }
}
```

---

## 📁 Project Structure

```
FastAPI-Books-Backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration settings
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   └── book.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   └── book.py
│   ├── routers/             # API route handlers
│   │   ├── __init__.py
│   │   └── books.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   └── book_service.py
│   ├── middleware/          # Custom middleware (Coming Soon)
│   │   └── error_handler.py
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── dependencies.py
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_books.py
├── .env                     # Environment variables
├── .gitignore
├── requirements.txt         # Project dependencies
├── README.md
└── LICENSE
```

---

## 🧪 Testing

Run tests using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_books.py
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions small and focused on a single responsibility

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- [x] Basic FastAPI setup
- [x] Project structure
- [x] README documentation

### Version 1.1 (Next Release)
- [ ] Complete book CRUD operations
- [ ] Database integration (SQLAlchemy + PostgreSQL)
- [ ] Input validation and sanitization
- [ ] Error handling middleware
- [ ] Logging system

### Version 1.2 (Planned)
- [ ] JWT authentication system
- [ ] User management (registration, login)
- [ ] Role-based access control
- [ ] Protected routes

### Version 2.0 (Future)
- [ ] Advanced search and filtering
- [ ] Pagination support
- [ ] Rate limiting
- [ ] API versioning
- [ ] Email notifications
- [ ] File upload for book covers
- [ ] Caching with Redis
- [ ] Background tasks with Celery

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**huzipro**

- GitHub: [@huzipro](https://github.com/huzipro)

---

## 📞 Support

If you have any questions or need help, please:

- Open an issue on GitHub
- Check the [API documentation](http://localhost:8000/docs)
- Review the existing issues and pull requests

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The amazing web framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation library
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation

---

<div align="center">

Made with ❤️ by [huzipro](https://github.com/huzipro)

⭐ Star this repository if you find it helpful!

</div>
