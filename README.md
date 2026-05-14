# sum-api

A secure RESTful API built with Python and Flask that calculates the sequential sum of a list of numbers. Protected by API key authentication via the X-API-KEY request header.

Python 3.x | Flask | REST API | API Key Auth

---

## Features
- POST /sum endpoint
- Accepts a JSON payload with a list of numbers
- Returns the sequential sum, count, and original list
- API key authentication (X-API-KEY header)
- Input validation with meaningful error messages

---

## Tech Stack
- Python 3.x
- Flask 3.0
- python-dotenv

---

## Setup Instructions

1. Clone the repository
   git clone https://github.com/YOUR_USERNAME/sum-api.git
   cd sum-api

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file in the project root
   API_KEY=mysecretkey123

4. Run the app

   Option A - Default (port 5000):
   python app.py

   Option B - Auto port (if 5000 is busy):
   start.bat
   This will automatically find a free port starting from 5000 and launch the server on it.

---

## API Reference

| Method | Endpoint | Description              |
|--------|----------|--------------------------|
| POST   | /sum     | Calculate sequential sum |

Request Headers:
- Content-Type: application/json
- X-API-KEY: your-api-key

Request Body:
{"numbers": [5, 10, 15]}

---

## Testing the API (PowerShell or CMD)

Test 1 - Successful request (200 OK):
curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -H "X-API-KEY: mysecretkey123" -d "{\"numbers\": [5, 10, 15]}"

Expected response:
{"result": 30, "count": 3, "numbers": [5, 10, 15]}

Test 2 - Missing API key (401 Unauthorized):
curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d "{\"numbers\": [5, 10, 15]}"

Expected response:
{"error": "Unauthorized"}

Note: If you used start.bat and the server is running on a different port (e.g. 5001), replace 5000 in the curl commands with that port number.

---

## Error Codes

| Code | Meaning                        |
|------|--------------------------------|
| 200  | Success                        |
| 400  | Bad request / invalid input    |
| 401  | Missing or wrong API key       |

---

## Important
- The .env file must contain: API_KEY=your-secret-key
