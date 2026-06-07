# AI DSS — Sustainable Farming Decision Support System

An AI-powered decision support system for sustainable agriculture. It combines crop recommendation ML models, environmental intelligence (weather, soil, location), a QSSM sustainability score, government scheme matching, and a Gemini-backed RAG chat assistant.

## Architecture

| Layer | Stack |
|-------|-------|
| Frontend | React 18, Vite, Tailwind CSS, Recharts, Leaflet |
| Backend API | FastAPI, SQLAlchemy, PostgreSQL |
| ML | scikit-learn / XGBoost models (joblib) |
| LLM / RAG | Google Gemini, LangChain, FAISS, HuggingFace embeddings |
| External APIs | NASA POWER (weather), SoilGrids (soil), OpenCage (geocoding) |

```
AI-DSS/
├── backend/          # FastAPI application
├── frontend/         # React + Vite UI
├── llm/              # RAG pipeline, prompts, vector store
├── models/           # Trained ML model artifacts (.pkl)
├── data/             # Knowledge base CSVs and rule JSON files
├── notebooks/        # EDA and model training notebooks
└── docs/             # Additional documentation
```

## Prerequisites

Install these on your machine before setting up the project:

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Backend, LLM, ML scripts |
| Node.js | 18+ | Frontend (Vite 5) |
| npm | 9+ | Frontend package manager |
| PostgreSQL | 14+ (or hosted, e.g. Neon) | Application database |
| Git | latest | Clone and version control |

Optional but useful:

- **Google AI Studio account** — for a Gemini API key (chat and explanations)
- **OpenCage account** — for reverse geocoding (district/state from lat/lon)
- **8 GB+ RAM** — loading embedding models and FAISS indexes for RAG

---

## Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI-DSS
```

### 2. Backend setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows
```

Install Python dependencies:

```bash
pip install --upgrade pip

pip install \
  fastapi uvicorn[standard] \
  sqlalchemy psycopg2-binary \
  pydantic python-dotenv \
  slowapi \
  "passlib[bcrypt]" "python-jose[cryptography]" \
  requests pandas numpy scikit-learn joblib xgboost \
  geoalchemy2 \
  langchain-community faiss-cpu sentence-transformers \
  google-genai
```

> `google-generativeai` is optional; the backend prefers `google-genai` but falls back to the legacy SDK if installed.

### 3. Environment variables

Copy the example files and fill in your own values. **Never commit real secrets to git.**

```bash
cp .env.example .env
cp frontend/.env.example frontend/.env
```

All backend settings are loaded from the **project root** `.env` via `backend/app/core/config.py`.

#### Backend (project root `.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `SECRET_KEY` | Yes | Random string for JWT signing |
| `GOOGLE_API_KEY` | Yes (for AI chat) | Google Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey) |
| `OPENCAGE_API_KEY` | Yes (for location) | OpenCage API key for reverse geocoding |
| `GEMINI_MODEL` | No | Primary model name (default: `gemini-2.5-flash`) |
| `GEMINI_FALLBACK_MODELS` | No | Comma-separated fallback models if the primary is unavailable |
| `GEMINI_TIMEOUT` | No | Request timeout in seconds (default: `30`) |
| `JWT_ALGORITHM` | No | JWT algorithm (default: `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No | Token lifetime in minutes (default: `60`) |
| `AWS_BUCKET_NAME` | No | S3 bucket name if using file storage |
| `CORS_ALLOW_ORIGINS` | No | Comma-separated frontend origins allowed by the API |
| `CORS_ALLOW_ORIGIN_REGEX` | No | Regex for additional allowed origins (e.g. ngrok tunnels) |

#### Frontend (`frontend/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `VITE_API_BASE_URL` | Yes | Backend API URL (default: `http://localhost:8000`) |

> **Security:** Use strong, unique values for `SECRET_KEY`, database credentials, and all API keys. Do not use defaults in any shared or deployed environment.

### 4. Database

1. Create a PostgreSQL database (local install or a hosted provider such as Neon).
2. Set `DATABASE_URL` in the project root `.env`:

   ```
   postgresql://<user>:<password>@<host>:<port>/<database>?sslmode=require
   ```

3. Initialize tables from the `backend` directory:

   ```bash
   cd backend
   python -m app.core.init_db
   python -m app.core.init_qssm_table
   ```

4. (Optional) Seed crop season reference data (Kharif, Rabi, Zaid — **not** user accounts):

   ```bash
   python -m app.core.seed_data
   ```

### 5. ML models

The recommendation engine expects trained artifacts under `models/`:

```
models/
├── crop_model/crop_model.pkl
├── yield_model/yield_model.pkl
├── risk_model/risk_model.pkl
├── encoders/label_encoders.pkl
└── qssm_model/...
```

`.pkl` files are gitignored. If they are missing locally, train them using the notebooks in `notebooks/` (`ML_Models.ipynb`, `LSTM_Forecasting.ipynb`, etc.) or obtain them from your team.

### 6. Vector store (RAG knowledge base)

Knowledge CSVs live under `data/knowledge_base/`. Build FAISS indexes before using chat or `/knowledge` search:

```bash
# From project root, with venv active
python llm/build_vector_store.py
```

This downloads the `sentence-transformers/all-MiniLM-L6-v2` embedding model on first run and writes indexes to `llm/vector_store/`.

### 7. Run the backend

```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API root: http://localhost:8000  
- Interactive docs: http://localhost:8000/docs  
- OpenAPI JSON: http://localhost:8000/openapi.json  

### 8. Run the frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

The UI opens at http://localhost:5173 (Vite default).

### 9. First use

1. Open http://localhost:5173  
2. **Register** a new account at `/register` (there are no pre-seeded demo logins)  
3. Complete **onboarding** (farmer and farm profile)  
4. Explore dashboards, recommendations, environment data, and the AI chat assistant  

---

## Authentication

There are **no built-in demo or default login credentials** in this repository. Every user must be created through registration.

### Create an account (UI)

1. Go to http://localhost:5173/register  
2. Choose a username and password  
3. Fill in farmer details (name, district, language, etc.)  
4. You are logged in automatically after registration  

### Create an account (API)

```bash
# Register
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "myuser", "password": "your-secure-password"}'

# Login (returns a JWT access token)
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "myuser", "password": "your-secure-password"}'
```

Use the returned `access_token` as a Bearer token for protected requests:

```bash
curl http://localhost:8000/farmer \
  -H "Authorization: Bearer <access_token>"
```

Tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default 60 minutes, set in `.env`).

If you already have an account in a shared database from a teammate, use those credentials — they are not documented here.

---

## Development

### Running tests

From the project root with the venv active:

```bash
# Example: chat enhancement tests
python -m pytest backend/app/test_chat_enhancements.py -v

# Other backend tests
python -m pytest backend/app/ -v --ignore=backend/app/examples_chat_responses.py
```

### Linting (frontend)

```bash
cd frontend
npm run lint
```

### Production build (frontend)

```bash
cd frontend
npm run build
npm run preview    # local preview of production build
```

The frontend includes a `vercel.json` for deployment on Vercel. Set `VITE_API_BASE_URL` in the Vercel project environment to your production API URL.

### Logs

Application logs are written to `logs/app.log` at the project root.

---

## API overview

| Area | Prefix / routes | Description |
|------|-----------------|-------------|
| Auth | `POST /register`, `POST /login` | User registration and JWT login |
| Farmer / Farm | `POST /farmer`, `POST /farm` | Profile and farm context |
| Environment | `GET /environment` | Weather, soil, and location for lat/lon |
| Recommendations | `POST /recommendation`, `POST /recommendation/explain` | Crop ML + LLM explanations |
| QSSM | QSSM routes | Sustainability scoring |
| History | `POST /history`, `GET /history/{farm_id}` | Decision history |
| Voice / Chat | `POST /voice` | RAG-powered agricultural assistant |
| Knowledge | `GET /knowledge/search/{domain}` | Vector search over knowledge base |

Full route list and request schemas: http://localhost:8000/docs

---

## External services

| Service | Used for | API key needed? |
|---------|----------|-----------------|
| Google Gemini | Chat, explanations, voice advisory | Yes (`GOOGLE_API_KEY`) |
| NASA POWER | Weather data | No (public API) |
| SoilGrids (ISRIC) | Soil properties | No (public API) |
| OpenCage | Reverse geocoding | Yes (`OPENCAGE_API_KEY` in `.env`) |
| PostgreSQL | Persistent storage | Yes (`DATABASE_URL` in `.env`) |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `AI not configured. Set GOOGLE_API_KEY` | Missing or empty Gemini key | Add `GOOGLE_API_KEY` to `.env` and restart the API |
| `Gemini SDK is not installed` | Missing package | `pip install google-genai` |
| Database connection errors | Wrong `DATABASE_URL` | Verify `DATABASE_URL` in `.env` and that PostgreSQL is reachable |
| Location data missing | OpenCage key not set | Add `OPENCAGE_API_KEY` to `.env` |
| `FileNotFoundError` for `.pkl` models | ML artifacts missing | Train or copy models into `models/` |
| RAG / chat returns generic answers | FAISS indexes missing | Run `python llm/build_vector_store.py` |
| CORS errors in browser | Frontend origin not allowed | Set `CORS_ALLOW_ORIGINS` or update defaults in `backend/app/main.py` |
| Frontend cannot reach API | Wrong base URL | Check `VITE_API_BASE_URL` in `frontend/.env` |
| `Invalid username` / `Invalid password` on login | No account or wrong credentials | Register at `/register` first; there is no default demo user |
| `Username already exists` on register | Account taken | Log in instead, or pick a different username |

---

## Additional documentation

- `docs/CHAT_ENHANCEMENT_GUIDE.md` — agricultural chat bot behavior and configuration  
- `CHAT_SYSTEM_UPDATE.md` — recent chat system changes  
- `projectplan.md` — phased development roadmap  
- `swagger_docs.json` — exported API reference  

---

## Security notes

- `.env` files are gitignored. Keep API keys, database passwords, and JWT secrets out of version control.
- Rotate `SECRET_KEY` and all third-party API keys before deploying publicly.
- The backend applies rate limiting via `slowapi`; tune limits in `backend/app/core/rate_limiter.py` if needed.
- Keep a single backend `.env` at the project root; do not commit it to version control.

---

## License

Add your license here if applicable.
