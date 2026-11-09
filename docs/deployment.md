# Deployment Guide — Travel Package CMS

## 1. Overview

Travel Package CMS is a full-stack application with:

- Next.js + React + TypeScript frontend
- FastAPI + Python backend
- PostgreSQL database
- Google Gemini as the primary AI provider
- Ollama + Phi-3 as the local AI fallback
- JWT authentication
- SQLAlchemy ORM
- Alembic database migrations

Repository:

https://github.com/sachint19004/travel-package-cms.git

---

## 2. Prerequisites

Install the following before deployment:

- Git
- Python 3.10+
- Node.js and npm
- PostgreSQL
- Ollama
- Phi-3 model for the local AI fallback

Optional but recommended:

- Docker / Docker Compose
- A reverse proxy such as Nginx for production

---

## 3. Clone the Repository

```bash
git clone https://github.com/sachint19004/travel-package-cms.git
cd travel-package-cms
```

---

## 4. Backend Deployment

```bash
cd backend
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
alembic upgrade head
```

Start FastAPI:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Backend API:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

For production, run the backend behind a reverse proxy and use HTTPS.

---

## 5. PostgreSQL Configuration

Create a PostgreSQL database and configure the backend connection string.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/travel_cms
```

Run:

```bash
alembic upgrade head
```

Do not commit database credentials to GitHub.

---

## 6. AI Configuration

### Gemini

Configure the Gemini API key through environment variables:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### Ollama

Install and start Ollama, then pull Phi-3:

```bash
ollama pull phi3
```

Verify:

```bash
ollama list
```

Example configuration:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=phi3
```

The application uses Gemini as the primary provider and Ollama/Phi-3 as the fallback when the primary provider is unavailable.

---

## 7. Frontend Deployment

```bash
cd frontend
npm install
npm run build
npm start
```

For local development:

```bash
npm run dev
```

The development frontend is normally available at:

```text
http://localhost:3000
```

For production, configure the frontend API base URL to point to the deployed FastAPI backend.

---

## 8. Environment Variables

Keep secrets outside source control.

Typical backend variables include:

```env
DATABASE_URL=postgresql://username:password@host:5432/travel_cms
JWT_SECRET_KEY=change_this_in_production
GEMINI_API_KEY=your_gemini_api_key
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=phi3
```

The exact variable names should match the project's current configuration.

Add local secret files to `.gitignore`:

```gitignore
.env
.env.*
venv/
__pycache__/
node_modules/
```

---

## 9. Production Architecture

```text
                    Internet
                       |
                       v
                ┌──────────────┐
                │ Reverse Proxy│
                │    HTTPS      │
                └──────┬───────┘
                       |
             ┌─────────┴─────────┐
             |                   |
             v                   v
      ┌─────────────┐     ┌─────────────┐
      │  Next.js    │     │   FastAPI   │
      │  Frontend   │     │   Backend   │
      └─────────────┘     └──────┬──────┘
                                  |
                    ┌─────────────┼─────────────┐
                    |             |             |
                    v             v             v
              PostgreSQL       Gemini       Ollama
              Database        Primary AI    Phi-3
                                             Fallback
```

---

## 10. Health Checks

Verify the backend:

```text
http://localhost:8000/docs
```

Verify the frontend:

```text
http://localhost:3000
```

Verify PostgreSQL connectivity through the application.

Verify Ollama:

```bash
ollama list
```

Test the AI extraction and recommendation endpoints through Swagger.

---

## 11. Recommended Production Practices

- Use HTTPS.
- Store secrets in environment variables or a secrets manager.
- Use a managed PostgreSQL instance where appropriate.
- Restrict database network access.
- Run the FastAPI application behind a production reverse proxy.
- Configure CORS for the deployed frontend domain instead of allowing arbitrary origins.
- Use production JWT secrets.
- Back up PostgreSQL regularly.
- Monitor backend errors and database health.
- Do not expose PostgreSQL directly to the public internet.
- Pin dependency versions for reproducible builds.

---

## 12. Deployment Verification Checklist

- [ ] Repository cloned successfully
- [ ] PostgreSQL database created
- [ ] Environment variables configured
- [ ] Alembic migrations completed
- [ ] FastAPI backend starts successfully
- [ ] Swagger is accessible
- [ ] Frontend builds successfully
- [ ] Frontend connects to backend
- [ ] Gemini API configured
- [ ] Ollama installed
- [ ] Phi-3 model available
- [ ] Gemini fallback tested
- [ ] Authentication tested
- [ ] Package CRUD tested
- [ ] Seasonal pricing tested
- [ ] Enquiry workflow tested
- [ ] AI extraction tested
- [ ] Package recommendation tested
- [ ] Production secrets excluded from Git
