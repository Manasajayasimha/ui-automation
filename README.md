# ui_automation
## Steps to run UI automation tests
1. Create venv `python3 -m venv .venv`
2. Activate venv `source .venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
3. Run command `export PYTHONPATH=/config:/locators:/pages:`
4. Run Test `pytest tests/test_homepage.py`