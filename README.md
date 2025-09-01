# FastAPI PostgreSQL Boilerplate with Docker 🚀

A production-ready FastAPI boilerplate with PostgreSQL database, Docker containerization, and Docker Compose orchestration. Perfect for rapid API development and deployment.

## 🌟 Features

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Robust relational database
- **Docker & Docker Compose** - Containerized development and deployment
- **Production Ready** - Configured for both development and production environments
- **Easy Setup** - Get started in minutes with minimal configuration

## 🚀 Quick Start

### Prerequisites

- Docker
- Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fastapi-postgres-boilerplate.git
   cd fastapi-postgres-boilerplate
   ```

2. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   # Database Configuration
   DATABASE_URL=postgresql://username:password@db:5432/database_name
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=your_database_name
   
   # Application Configuration
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

3. **Start the application**
   ```bash
   docker-compose up --build
   ```

4. **Access your API**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## 📁 Project Structure

```
fastapi-postgres-boilerplate/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── models/              # Database models
│   ├── routers/             # API route handlers
│   ├── schemas/             # Pydantic schemas
│   ├── database.py          # Database configuration
│   └── config.py            # Application configuration
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker container definition
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@db:5432/dbname` |
| `POSTGRES_USER` | PostgreSQL username | `postgres` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `password` |
| `POSTGRES_DB` | PostgreSQL database name | `fastapi_db` |
| `SECRET_KEY` | Application secret key | Required |
| `DEBUG` | Enable debug mode | `False` |

### Database Setup

The boilerplate includes automatic database initialization. Your PostgreSQL database will be created when you run `docker-compose up`.

## 🐳 Docker Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Rebuild containers
docker-compose up --build

# Stop services
docker-compose down

# View logs
docker-compose logs

# Access database
docker-compose exec db psql -U your_username -d your_database_name
```

## 📚 API Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🚀 Deployment

This boilerplate is ready for deployment on:

- **AWS ECS**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**
- **Heroku**
- **Any Docker-compatible hosting**

## 🛠️ Development

### Adding New Routes

1. Create a new router in `app/routers/`
2. Import and include it in `app/main.py`
3. Define your Pydantic schemas in `app/schemas/`
4. Create database models in `app/models/`

### Database Migrations

```bash
# Install Alembic for migrations
pip install alembic

# Initialize Alembic
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migration
alembic upgrade head
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Keywords

`fastapi` `postgresql` `docker` `docker-compose` `python` `api` `boilerplate` `microservice` `rest-api` `backend` `web-framework` `database` `containerization` `devops` `production-ready`

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**FastAPI PostgreSQL Docker Boilerplate** - The fastest way to build production-ready APIs with Python, PostgreSQL, and Docker. Perfect for startups, enterprises, and individual developers looking for a robust foundation for their next project.