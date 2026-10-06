python3 -m venv .venv

python3 -m pip install "fastapi[standard]" pytest
source .venv/bin/activate

python -m pytest 'test_file_name.py'
