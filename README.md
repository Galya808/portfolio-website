# Personal Portfolio Website

A production-deployed full-stack portfolio for presenting my projects, technical
skills, education, and experience.

[View the live website](https://galymzhan.xyz) ·
[View my GitHub profile](https://github.com/Galya808)

![Portfolio homepage](./cv-frontend/public/projects/portfolio-home.png)

## Overview

The application combines a responsive Next.js interface with a FastAPI REST API
and PostgreSQL database. Portfolio content is retrieved from the API, while
write operations are protected with JWT authentication.

The production application runs on AWS EC2 behind Nginx. The frontend and
backend are managed as separate systemd services.

## Features

- Responsive single-page portfolio with animated section transitions.
- Project cards with screenshots, technology tags, source links, and live demos.
- Skills grouped by backend, frontend, database, testing, security, DevOps,
  cloud, and observability categories.
- Education, experience, About, and Contact sections backed by API data.
- Downloadable résumé served directly by the production website.
- SEO metadata, Open Graph previews, `robots.txt`, and `sitemap.xml`.
- JWT-protected content-management endpoints.
- Repository, service, and strategy layers for backend business logic.
- Automated backend tests and frontend lint/build validation.
- Structured application logging and configurable project sorting.

## Architecture

```mermaid
flowchart LR
    Browser["Browser"] --> Nginx["Nginx reverse proxy"]
    Nginx --> Next["Next.js frontend"]
    Nginx --> API["FastAPI API"]
    Next --> API
    API --> Services["Service layer"]
    Services --> Repositories["Repository layer"]
    Repositories --> PostgreSQL[(PostgreSQL)]
```

## Technology Stack

| Area | Technologies |
|---|---|
| Frontend | Next.js 16, React 19, TypeScript, Tailwind CSS, Framer Motion, Axios |
| Backend | Python, FastAPI, Pydantic, SQLAlchemy |
| Data | PostgreSQL |
| Authentication | JWT, bcrypt |
| Testing | pytest, HTTPX, pytest-cov, ESLint, Next.js production build |
| Production | AWS EC2, Nginx, Uvicorn, systemd |

## Repository Structure

```text
portfolio-website/
├── cv-backend/
│   ├── app/
│   │   ├── repositories/  # Database access
│   │   ├── routers/       # FastAPI routes
│   │   ├── services/      # Business logic
│   │   ├── strategies/    # Project sorting strategies
│   │   ├── auth.py        # Password and JWT utilities
│   │   ├── database.py    # SQLAlchemy configuration
│   │   ├── main.py        # FastAPI application
│   │   ├── models.py      # Database models
│   │   └── schemas.py     # Request and response schemas
│   ├── tests/
│   └── requirements.txt
└── cv-frontend/
    ├── app/               # Next.js App Router and metadata routes
    ├── components/        # Portfolio sections
    ├── hooks/             # Client-side data loading
    ├── lib/               # API client functions
    ├── public/            # Static public assets
    └── types/             # Shared TypeScript types
```

## API Overview

Public read endpoints provide project, skill, experience, and education data.
Content changes require a bearer token obtained from the login endpoint.

| Method | Endpoint | Purpose | Authentication |
|---|---|---|---|
| `POST` | `/api/auth/login` | Obtain an access token | No |
| `GET` | `/api/projects/` | List projects | No |
| `POST` | `/api/projects/` | Create a project | Yes |
| `DELETE` | `/api/projects/{id}` | Delete a project | Yes |
| `GET` | `/api/skills/` | List skills | No |
| `POST` | `/api/skills/` | Create a skill | Yes |
| `PATCH` | `/api/skills/{id}` | Update a skill | Yes |
| `GET` | `/api/experience/` | List experience | No |
| `GET` | `/api/education/` | List education | No |

Public registration is intentionally disabled. Administrative users must be
created through a trusted server-side process.

## Run Locally

### Prerequisites

- Python 3.13 or newer
- Node.js 20 or newer
- PostgreSQL

### Backend

From the repository root:

```bash
cd cv-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `cv-backend/.env`:

```dotenv
DATABASE_URL=postgresql://USER:PASSWORD@localhost:5432/DATABASE
SECRET_KEY=replace-with-a-long-random-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379/0
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

### Frontend

In another terminal:

```bash
cd cv-frontend
npm ci
npm run dev
```

Open `http://localhost:3000`. During local development, Next.js proxies
`/api/*` requests to the FastAPI server on port `8000`.

## Quality Checks

Run backend tests:

```bash
cd cv-backend
./venv/bin/pytest -q
```

Run frontend validation:

```bash
cd cv-frontend
npm run lint
npm run build
```

## Production Deployment

The current production environment uses:

- Nginx for TLS termination and reverse proxying.
- `frontend.service` for the Next.js application.
- `backend.service` for the Uvicorn/FastAPI application.
- PostgreSQL for persistent portfolio content.

A typical server update is:

```bash
git pull --ff-only origin main
cd cv-backend && ./venv/bin/pip install -r requirements.txt
cd ../cv-frontend && npm ci && npm run build
sudo systemctl restart backend.service frontend.service
```

Production secrets and the résumé PDF are intentionally excluded from Git.

## Security Notes

- Secrets are loaded from environment variables and are never committed.
- Passwords are stored as hashes.
- Administrative write operations require a signed JWT.
- Public user registration is disabled.
- CORS is restricted to local development and the production domain.
- The production résumé is deployed directly rather than stored in the public
  repository.

## Project Status

The website is live and actively maintained. Current development is focused on
content administration, frontend resilience, accessibility, and deployment
automation.
