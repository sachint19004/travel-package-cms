# ✈️ Travel Package CMS

![Homepage](docs/homepage.png)

## Overview

Travel Package CMS is a full-stack AI-powered travel management platform designed for travel consultants and agencies.

The platform enables administrators to manage travel packages, pricing, and customer enquiries while leveraging AI to extract traveller requirements and recommend suitable travel packages.

---

## Features

### 🔐 Authentication

- JWT Authentication
- Secure Admin Login API
- Current User Endpoint
- Role-ready Authorization Architecture

### 📦 Package Management

- Create Packages
- Update Packages
- Delete Packages
- View Package Details
- Package Version History

### 💰 Seasonal Pricing

- Seasonal Price Management
- Dynamic Pricing Support

### 📩 Enquiry Management

- Customer Enquiry Inbox
- Enquiry Tracking
- AI-Enhanced Enquiry Processing

### 🤖 AI Features

#### Enquiry Extraction

The AI extracts structured traveller requirements from customer enquiries, including:

- Destination
- Budget
- Number of nights
- Number of travellers
- Traveller preferences
- Confidence Score

Example:

```json
{
  "destination": "Kerala",
  "adults": 2,
  "children": 1,
  "budget": "1.2 lakh",
  "month": "December"
}
```

#### Package Recommendations

The platform automatically suggests the most relevant travel packages based on enquiry details.

The recommendation workflow uses extracted traveller requirements such as:

- Destination
- Budget
- Duration
- Number of travellers
- Travel month
- Preferences

to identify suitable travel packages.

---

## 🧠 AI Architecture

### Primary AI Provider

Google Gemini

### Fallback AI Provider

Ollama (Phi-3)

If Gemini becomes unavailable, the platform automatically falls back to a locally hosted model through Ollama.

This provides resilience in the AI pipeline and allows enquiry processing to continue when the primary external AI provider is unavailable.

---

## 🛠️ Technology Stack

### Frontend

- Next.js
- React
- TypeScript

### Backend

- FastAPI
- SQLAlchemy
- Alembic
- Python

### Database

- PostgreSQL

### AI

- Google Gemini
- Ollama
- Phi-3

---

## 🏗️ Project Architecture

```text
                         ┌───────────────────────┐
                         │      Frontend         │
                         │    Next.js + React    │
                         └───────────┬───────────┘
                                     │
                                     │ HTTP / REST API
                                     ▼
                         ┌───────────────────────┐
                         │       Backend         │
                         │       FastAPI         │
                         └───────────┬───────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
             ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
             │ PostgreSQL  │ │   Gemini    │ │   Ollama     │
             │  Database   │ │ Primary AI  │ │  Phi-3       │
             └─────────────┘ └─────────────┘ │  Fallback    │
                                             └──────────────┘
```

---

## 🚀 Implemented Modules

### Backend

- ✅ Authentication
- ✅ Package CRUD
- ✅ Seasonal Pricing
- ✅ Version History
- ✅ Enquiry Management
- ✅ AI Extraction
- ✅ AI Recommendations
- ✅ Gemini Integration
- ✅ Ollama Fallback

### Frontend

- ✅ Home Page
- ✅ Public Package Listing
- ✅ Package Details Page
- ✅ Admin Package Dashboard
- ✅ Admin Enquiry Dashboard

---

## 🔌 API Endpoints

### Authentication

```http
POST /auth/login
GET /auth/me
```

### Packages

```http
POST /packages/
GET /packages/
GET /packages/{package_id}
PUT /packages/{package_id}
DELETE /packages/{package_id}
```

### Package Versions

```http
GET /packages/{package_id}/versions
```

### Pricing

```http
POST /pricing/{package_id}
GET /pricing/{package_id}
```

### Enquiries

```http
POST /enquiries/
GET /enquiries/
GET /enquiries/{id}
```

### AI

```http
POST /ai/extract
POST /ai/suggest
```

---

## ⚙️ Local Setup

### Prerequisites

Make sure the following are installed:

- Python 3.10+
- Node.js
- npm
- PostgreSQL
- Ollama

---

## 🔧 Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
alembic upgrade head
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

---

## 🎨 Frontend Setup

Open a new terminal.

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:3000
```

---

## 🤖 Ollama Setup

Ollama is used as the local fallback AI provider.

Install Ollama and make sure the Ollama service is running.

Pull the Phi-3 model:

```bash
ollama pull phi3
```

Verify that the model is available:

```bash
ollama list
```

The application can use the locally hosted Phi-3 model through Ollama when Gemini is unavailable.

---

## 🔑 Environment Variables

Create the required environment configuration file in the backend according to your project setup.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/travel_cms

JWT_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

OLLAMA_BASE_URL=http://localhost:11434

OLLAMA_MODEL=phi3
```

> **Important:** Never commit API keys, passwords, database credentials, JWT secrets, or other sensitive information to GitHub.

Add your environment file to `.gitignore`:

```gitignore
.env
.env.*
venv/
__pycache__/
node_modules/
```

---

## 🔄 AI Workflow

The AI enquiry processing pipeline works as follows:

```text
Customer Enquiry
       |
       v
Gemini Extraction
       |
       +----------------------+
       |                      |
       | Success              | Failure
       |                      |
       v                      v
Structured Data         Ollama (Phi-3)
       |                      |
       |                      v
       |               Structured Data
       |                      |
       +----------+-----------+
                  |
                  v
        Package Recommendation
```

---

## 🧩 Example AI Workflow

A customer may submit an enquiry such as:

```text
"We are a family of 3 planning a trip to Kerala
in December. We have a budget of around 1.2 lakh
and would like a comfortable 5-night trip."
```

The AI can extract structured information such as:

```json
{
  "destination": "Kerala",
  "adults": 2,
  "children": 1,
  "nights": 5,
  "budget": "1.2 lakh",
  "month": "December",
  "preferences": [
    "comfortable accommodation"
  ]
}
```

The extracted information can then be passed to the recommendation workflow to identify relevant travel packages.

---

## 📊 Package Recommendation Flow

```text
                 Customer Enquiry
                        |
                        v
             Extract Traveller Details
                        |
                        v
       +----------------+----------------+
       |                |                |
       v                v                v
  Destination        Budget          Duration
       |                |                |
       +----------------+----------------+
                        |
                        v
              Traveller Preferences
                        |
                        v
              Available Packages
                        |
                        v
              Seasonal Pricing
                        |
                        v
             Package Matching
                        |
                        v
              Recommendation
```

---

## 🗃️ Package Management

Administrators can manage travel packages through the admin dashboard.

Supported operations include:

- Create a travel package
- View travel packages
- View individual package details
- Update package information
- Delete packages
- Manage seasonal pricing
- View package version history

---

## 💰 Seasonal Pricing

The system supports seasonal pricing for travel packages.

This allows administrators to maintain different prices based on travel periods or seasons.

Example:

```text
Package
   |
   +---- Base Price
   |
   +---- Summer Pricing
   |
   +---- Winter Pricing
   |
   +---- Holiday Pricing
```

This pricing information can also be used during package recommendation.

---

## 📩 Enquiry Management

The enquiry management module provides an interface for administrators to view and track customer enquiries.

An enquiry can contain natural-language information such as:

```text
"We are looking for a 5-day trip to Kerala
for two adults and one child in December.
Our budget is around ₹1.2 lakh."
```

The AI processing pipeline can convert this unstructured enquiry into structured information.

```text
Natural Language Enquiry
          |
          v
     AI Extraction
          |
          v
 Structured Traveller Data
          |
          v
 Package Recommendation
```

---

## 🔐 Authentication

The backend uses JWT-based authentication for protected API access.

Authentication flow:

```text
Admin Login
     |
     v
POST /auth/login
     |
     v
JWT Token
     |
     v
Authenticated API Requests
     |
     v
Protected Admin Resources
```

The current authenticated user can be retrieved through:

```http
GET /auth/me
```

---

## 🧱 Database

The application uses PostgreSQL as its primary relational database.

SQLAlchemy is used as the ORM layer, while Alembic manages database migrations.

The database stores application data such as:

- Users
- Travel packages
- Package versions
- Seasonal pricing
- Customer enquiries
- Related application records

---

## 📁 Project Structure

```text
travel-package-cms/
│
├── README.md
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── alembic/
│   ├── requirements.txt
│   └── ...
│
├── docs/
│   └── homepage.png
│
└── .gitignore
```

---

## 📸 Screenshots

### Homepage

![Homepage](docs/homepage.png)

---

## 🔌 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

```text
http://localhost:8000/docs
```

The Swagger interface allows developers to:

- View available endpoints
- Inspect request schemas
- Test API endpoints
- View response structures
- Test authenticated APIs

---

## 🧪 API Testing

The API can be tested using:

- Swagger UI
- Postman
- curl
- Frontend API integration

Swagger is available at:

```text
http://localhost:8000/docs
```

---

## 🛡️ Security

The platform includes:

- JWT-based authentication
- Protected admin APIs
- Environment-based configuration
- Secure secret management through environment variables
- Separation of frontend and backend services
- Database-backed authentication architecture

Sensitive credentials should always be stored in environment variables and excluded from version control.

---

## 🔄 Gemini + Ollama Fallback

The application is designed with a primary/fallback AI architecture.

### Normal Flow

```text
User Enquiry
     |
     v
Google Gemini
     |
     v
Structured Traveller Data
     |
     v
Package Recommendation
```

### Fallback Flow

```text
User Enquiry
     |
     v
Google Gemini
     |
     X
     |
     v
Ollama
     |
     v
Phi-3
     |
     v
Structured Traveller Data
     |
     v
Package Recommendation
```

This approach improves reliability by providing a local AI alternative.

---

## 🎯 Business Use Case

Travel consultants often receive customer enquiries in natural language.

For example:

```text
"Need a 6-day Kerala trip for 4 people
in December. Budget is around ₹1.5 lakh.
We prefer beaches and comfortable hotels."
```

Manually extracting these requirements and searching through available packages can take time.

The Travel Package CMS automates part of this workflow:

```text
Customer Enquiry
       |
       v
AI Requirement Extraction
       |
       v
Structured Traveller Profile
       |
       v
Package Matching
       |
       v
Recommended Packages
```

This can help travel consultants process enquiries faster and reduce repetitive manual work.

---

## 📈 Future Enhancements

Potential future improvements include:

- 🔒 Frontend Route Protection
- 🤖 AI Draft Reply Generation
- 📄 PDF Quote Generation
- 📧 Email Automation
- 👥 Multi-Role Access Control
- 🚀 Deployment Pipeline
- 🎯 Advanced Recommendation Scoring
- 📊 Analytics Dashboard
- 🔔 Automated Enquiry Notifications
- ☁️ Cloud Deployment
- 📱 Mobile-Friendly Admin Experience
- 💬 AI Chat Assistant for Customers

---

## 🌐 Deployment

The application can be deployed using a separated frontend/backend architecture.

Example deployment structure:

```text
                    Internet
                       |
                       v
              ┌─────────────────┐
              │    Frontend     │
              │    Next.js      │
              └────────┬────────┘
                       |
                       v
              ┌─────────────────┐
              │     Backend     │
              │     FastAPI     │
              └───────┬─────────┘
                      |
          +-----------+-----------+
          |                       |
          v                       v
   ┌─────────────┐         ┌─────────────┐
   │ PostgreSQL  │         │ AI Provider │
   │  Database   │         │ Gemini /    │
   │             │         │ Ollama      │
   └─────────────┘         └─────────────┘
```

Possible deployment targets include cloud platforms supporting:

- Next.js
- FastAPI
- PostgreSQL
- Docker
- Environment-based configuration

---

## 🧰 Development Tools

| Category | Technology |
|----------|------------|
| Frontend | Next.js |
| UI | React |
| Language | TypeScript |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Database | PostgreSQL |
| AI | Google Gemini |
| AI Fallback | Ollama / Phi-3 |
| API | REST |
| Authentication | JWT |

---

## 📌 Key Highlights

The project combines traditional travel-management functionality with AI-powered automation.

### Traditional CMS Capabilities

- Travel package management
- Package version history
- Seasonal pricing
- Customer enquiry management
- Admin dashboards
- Authentication

### AI Capabilities

- Natural-language enquiry processing
- Traveller requirement extraction
- Structured JSON generation
- Confidence scoring
- Package recommendations
- Gemini integration
- Local Ollama fallback

### Engineering Capabilities

- RESTful API architecture
- FastAPI backend
- PostgreSQL database
- SQLAlchemy ORM
- Alembic migrations
- JWT authentication
- Next.js frontend
- AI provider fallback architecture

---

## 📋 API Summary

| Module | Method | Endpoint |
|--------|--------|----------|
| Authentication | POST | `/auth/login` |
| Authentication | GET | `/auth/me` |
| Packages | POST | `/packages/` |
| Packages | GET | `/packages/` |
| Packages | GET | `/packages/{package_id}` |
| Packages | PUT | `/packages/{package_id}` |
| Packages | DELETE | `/packages/{package_id}` |
| Versions | GET | `/packages/{package_id}/versions` |
| Pricing | POST | `/pricing/{package_id}` |
| Pricing | GET | `/pricing/{package_id}` |
| Enquiries | POST | `/enquiries/` |
| Enquiries | GET | `/enquiries/` |
| Enquiries | GET | `/enquiries/{id}` |
| AI | POST | `/ai/extract` |
| AI | POST | `/ai/suggest` |

---

## 👨‍💻 Author

**Sachin T**

AI-Powered Travel Package CMS

---

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.

---

## 🚀 Getting Started Quickly

For a quick local setup:

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd travel-package-cms
```

### 2. Start the backend

```bash
cd backend

python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
alembic upgrade head
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

### 3. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

### 4. Start Ollama

Make sure Ollama is running and Phi-3 is available:

```bash
ollama pull phi3
```

### 5. Open the application

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## 📸 Adding Screenshots

Create a `docs` directory in the root of the repository:

```text
travel-package-cms/
└── docs/
```

Place your homepage screenshot inside it:

```text
travel-package-cms/
└── docs/
    └── homepage.png
```

The README references the screenshot using:

```markdown
![Homepage](docs/homepage.png)
```

GitHub will automatically render the image when the README is viewed.

---

## 📝 Git Commit

After creating the README and adding the screenshot:

```bash
git add README.md docs/
```

Commit:

```bash
git commit -m "docs: add project documentation and screenshots"
```

Push:

```bash
git push
```

---

## ✅ Final Submission Checklist

- [x] Backend Complete
- [x] Frontend Complete
- [x] Authentication Implemented
- [x] Package CRUD Implemented
- [x] Seasonal Pricing Implemented
- [x] Version History Implemented
- [x] Enquiry Management Implemented
- [x] AI Extraction Implemented
- [x] AI Recommendations Implemented
- [x] Gemini Integration
- [x] Ollama Fallback
- [x] PostgreSQL Database
- [x] Swagger API Documentation
- [x] README.md
- [x] Homepage Screenshot
- [x] `.gitignore`
- [x] GitHub Push

---

## 🎉 Project Summary

Travel Package CMS demonstrates how a traditional travel-management system can be enhanced using modern web technologies and AI.

The platform combines:

**Next.js + React + TypeScript**

with

**FastAPI + PostgreSQL + SQLAlchemy**

and

**Google Gemini + Ollama (Phi-3)**

to provide a complete AI-powered workflow for managing travel packages and processing customer enquiries.

The combination of package management, seasonal pricing, enquiry tracking, AI extraction, package recommendations, and AI fallback makes the platform suitable as a full-stack AI engineering project.
