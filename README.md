# Court-Data Fetcher & Mini-Dashboard

## ✅ Project Summary
Delhi High Court Case Scraper
This project is a simple Flask web application that scrapes case status information from the official Delhi High Court website using Selenium.

✅ It allows users to:

Select a Case Type

Enter Case Number & Filing Year

View case status details

Optionally download the page

🛠️ Tech Stack
Python 3

Flask

Selenium (Web Automation)

ChromeDriver

HTML/CSS (Frontend)

SQLite (for query history)

🚀 How to Run the App
Clone this repo:
git clone https://github.com/SuryaKumarV20/delhi-high-court-scraper.git
cd delhi-high-court-scraper

(Optional) Create a virtual environment:
python -m venv venv
venv\Scripts\activate (on Windows)

Install dependencies:
pip install -r requirements.txt

Set up database:
Open Python shell and run:
from db import init_db
init_db()

Download ChromeDriver

Download matching ChromeDriver from https://chromedriver.chromium.org/downloads

Place it inside chromedriver-win64/

Run the Flask app:
python app.py

Open in browser:
http://127.0.0.1:5000

🤖 CAPTCHA Bypass Strategy
The Delhi High Court website doesn’t enforce CAPTCHA for direct case search links. Therefore, no special CAPTCHA bypass or token is needed.

📁 .env.example
This file is a template for environment variables:

.env.example

Flask secret key (optional, used if sessions/CSRF used)
SECRET_KEY=your-secret-key

🖼️ UI Preview
You’ll see a clean input form where you can:

Select Case Type (e.g., Writ Petition - Civil)

Enter Case Number (e.g., 123)

Enter Filing Year (e.g., 2023)

Hit Submit → Scraper will launch in background and return the HTML content.
