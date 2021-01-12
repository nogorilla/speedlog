# Description
Use this to monitor your internet speeds.


# Installation
1. Create a virtual environment: `python3 -m venv venv`
2. Activate virtualenv: `source venv/bin/activate`
3. Install required packages: `pip install -r requirements.txt`
4. Copy `speedlog.example.db` to `speedlog.db`
5. Create a cron task to call `python3 monitor.py` at your desired interval