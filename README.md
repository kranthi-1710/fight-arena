# Fight Arena
# Fight Arena

Backend for an online 2D fighting game platform, built with Python and FastAPI. It will power player accounts, a ranked ladder, match history and live 1v1 matches.

## Features so far

- Player registration with bcrypt-hashed passwords
- Login that returns a signed JWT access token
- Protected endpoints that require a valid token (`GET /me`)
- SQLite database managed with SQLAlchemy

## Tech stack

Python, FastAPI, SQLAlchemy, SQLite, Pydantic, passlib (bcrypt), python-jose (JWT)

## Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| GET | `/` | Welcome message | No |
| POST | `/players` | Register a player | No |
| GET | `/players` | List players | No |
| POST | `/login` | Log in, get an access token | No |
| GET | `/me` | Current player's details | Yes |

## Run locally

1. Clone the repo and create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project folder with a secret key:
   ```
   SECRET_KEY=your-random-secret-key
   ```
   Generate one with `python -c "import secrets; print(secrets.token_hex(32))"`.
3. Start the server:
   ```
   uvicorn main:app --reload
   ```
4. Open http://127.0.0.1:8000/docs to try the API in Swagger.

## Roadmap

- Match history and result reporting
- Elo-style rating updates and ranked ladder
- Live 1v1 matches over WebSockets