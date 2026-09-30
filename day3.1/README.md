python -m pip install "fastapi[standard]"
python3 -m venv .venv
source .venv/bin/activate

fastapi dev main.py --port 8000
