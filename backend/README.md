# AI Smart Campus Security System - FastAPI Backend

This folder contains the FastAPI backend starter for the Final Year Project **AI Smart Campus Security System**.

## Current backend status

The backend starter is working and includes:

- FastAPI app setup
- SQLite database connection
- Health check API
- Basic project structure for future integration

## Tech stack

- FastAPI
- SQLite
- SQLModel
- Uvicorn

## Folder structure

```text
ai_smart_campus_security/
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── campus_security.db
```

## Files included

### `main.py`
Contains:
- FastAPI app initialization
- root API endpoint
- `/health` API endpoint

### `database.py`
Contains:
- SQLite connection
- SQLModel engine setup
- session generator
- database table creation function

### `requirements.txt`
Contains Python dependencies required to run the backend.

## How to run

### 1. Create virtual environment

```powershell
python -m venv venv
```

### 2. Activate virtual environment

```powershell
.\venv\Scripts\Activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
pip install fastapi-cli
```

### 4. Run backend server

Use either of these commands:

```powershell
python -m fastapi dev main.py
```

or

```powershell
python -m uvicorn main:app --reload
```

## Test API

Open in browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

## Current API response examples

### Root endpoint
```json
{
  "message": "AI Smart Campus Security System backend is running"
}
```

### Health endpoint
```json
{
  "status": "ok",
  "service": "backend",
  "database": "connected"
}
```

## Future integration

This backend will later connect with:

- Flutter frontend
- Geofencing module
- InsightFace face recognition module
- campus entry logs
- alert system
- attendance system

## Notes

- This is the backend starter only.
- Flutter frontend can be kept in a separate `frontend` folder in the main project repository.
- Other team members can build their modules separately and integrate them later with this backend.

## GitHub pull request note

This folder is ready for an initial pull request as a backend starter module.