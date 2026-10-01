python3 -m venv .venv
source .venv/bin/activate
python -m pip install "fastapi[standard]"
fastapi dev main.py --port 8000 