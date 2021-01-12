# Description
Use this to monitor your internet speeds.


# Installation
1. Create a virtual environment: `python3 -m venv venv`
2. Install required packages: `pip install -r requirements.txt`
3. Copy `speedlog.example.db` to `speedlog.db`
4. Create a cron task to call `python3 monitor.py` at your desired interval