# MoStar API

This repository provides a minimal FastAPI application used to proxy chat messages to the OpenAI API. The project includes a simple development environment and some database tooling via Alembic.

## Development Setup

1. **Create and activate a virtual environment (optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # For development and testing
   pip install -r requirements-dev.txt
   ```
3. **Create environment file**
   ```bash
   cp .env.example .env
   # edit .env and set `OPENAI_KEY` with your API key
   ```
4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```
5. **Start the application**
   ```bash
   uvicorn main:app --reload
   ```

## Running Tests

Tests use `pytest`. After installing the development requirements, run:

```bash
pytest
```
